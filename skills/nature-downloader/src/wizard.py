"""Configuration wizard module.

7-step interactive configuration flow for AI invocation.
Each step returns a prompt to the user and receives user input for validation.

Usage (AI invocation):
    from wizard import Wizard
    w = Wizard()
    # Step 1
    prompt = w.start()                # Prompt returned to user
    # After user answers
    result = w.handle_step1(user_input)
    # result = {"next": "step2"|"retry"|"done", "prompt": str, "data": dict}

Also supports non-interactive direct construction:
    w = Wizard()
    w.configure_from_preset("SJTU")  # One-click preset configuration
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from urllib.parse import parse_qs, urlparse

from config import save_config, backup_config, delete_config, CONFIG_FILE
from schools_loader import match_school, list_school_names
from validators import (
    KNOWN_DATABASES,
    validate_carsi_entry,
    validate_ezproxy_url,
    validate_libraries,
    validate_school_name,
    validate_sso_domain,
)


def infer_access_from_url(url: str) -> dict[str, Any]:
    """Infer the likely library access route from a user-provided resource URL."""
    raw_url = url.strip()
    parsed = urlparse(raw_url if "://" in raw_url else f"https://{raw_url}")
    host = parsed.netloc.lower()
    path = parsed.path.lower()
    query = parse_qs(parsed.query)
    service = query.get("service", [""])[0]
    service_host = urlparse(service).netloc.lower() if service else ""

    result: dict[str, Any] = {
        "resource_entry": raw_url,
        "entry_host": host,
        "entry_type": "resource_entry",
        "auth_type": "custom",
        "sso_domain": host,
        "service_host": service_host or None,
        "institution_hint": None,
        "notes": "",
    }

    if "metaersp" in host or "metaauth" in host:
        result.update(
            {
                "entry_type": "resource_portal",
                "auth_type": "cas",
                "sso_domain": "cas.whu.edu.cn" if host.startswith("whu.") else host,
                "institution_hint": host.split(".", 1)[0] if "." in host else None,
                "notes": "Resource aggregation portal; enter through this portal first, redirecting to unified authentication if necessary.",
            }
        )
    elif "/authserver/login" in path or host.startswith("cas."):
        hint = None
        if service_host:
            service_parts = urlparse(service).path.strip("/").split("/")
            if len(service_parts) >= 2:
                hint = service_parts[1]
        result.update(
            {
                "entry_type": "cas_login",
                "auth_type": "cas",
                "sso_domain": host,
                "institution_hint": hint,
                "notes": "CAS login entry; if service points to resource aggregation platform, return there to access databases.",
            }
        )
    elif "ezproxy" in host or "libproxy" in host:
        result.update({"entry_type": "ezproxy", "auth_type": "custom", "notes": "Library remote access proxy entry."})
    elif "webvpn" in host or "vpn" in host:
        result.update({"entry_type": "webvpn", "auth_type": "custom", "notes": "WebVPN entry."})
    elif "shibboleth" in path or "carsi" in host:
        result.update({"entry_type": "carsi", "auth_type": "sso", "notes": "CARSI/Shibboleth institutional authentication entry."})

    return result


class Wizard:
    """Configuration wizard state machine.

    State transitions:
        step1 (institution name) ->
            matched preset -> step4 (database confirmation) -> step6 (self-check) -> step7 (save)
            not matched -> step2 (CARSI check) -> step3 (SSO domain) -> step4 -> step6 -> step7
                                                   or step5 (EZproxy) -> step6 -> step7
    """

    def __init__(self) -> None:
        self.state: str = "step1"
        self.data: dict[str, Any] = {}
        self.matched_preset: Optional[dict[str, Any]] = None

    # ===== Step 1: Ask for institution name =====
    def start(self) -> str:
        """Return initial prompt."""
        self.state = "step1"
        return (
            "Hello! I am the literature download assistant. First-time use requires configuring your library resource entry (only once).\n\n"
            "Please send the platform link you normally use to access library electronic resources/databases.\n"
            "It can be a resource portal, database list, Web of Science entry, a database details page, "
            "or a login link that redirects to unified identity authentication.\n\n"
            "I will first determine the authorization path (CAS/CARSI/EZproxy/WebVPN/aggregation portal) based on the link; "
            "institution presets serve as a supplementary fallback."
        )

    def handle_step1(self, user_input: str) -> dict[str, Any]:
        """Process resource entry link; non-URL input falls back to institution preset lookup."""
        value = user_input.strip()
        if not value:
            return {"next": "retry", "prompt": "Input cannot be empty. Please paste your library electronic resource or database entry link:"}

        if "://" in value or "." in value:
            inferred = infer_access_from_url(value)
            self.data.update(inferred)
            self.data["school_name"] = inferred.get("institution_hint") or inferred["entry_host"]
            self.data["source"] = "resource_url"
            self.data["auth_type"] = inferred["auth_type"]
            self.data["sso_domain"] = inferred["sso_domain"]
            self.data["carsi_entry"] = inferred["resource_entry"]
            self.data["libraries"] = ["Web of Science", "ScienceDirect", "Springer", "IEEE Xplore", "CNKI", "ACS"]
            self.data["notes"] = inferred.get("notes", "")
            self.data["discovery"] = {"resource_entry_url": inferred["resource_entry"]}
            if inferred["entry_type"] == "resource_portal":
                self.data["discovery"]["resource_portal_url"] = inferred["resource_entry"]
            if inferred.get("service_host"):
                self.data["discovery"]["auth_service_host"] = inferred["service_host"]

            self.state = "step4"
            return {
                "next": "step4",
                "prompt": (
                    "Authorization path identified from resource link:\n"
                    f"  Entry type: {inferred['entry_type']}\n"
                    f"  Auth type: {inferred['auth_type']}\n"
                    f"  SSO domain: {inferred['sso_domain']}\n"
                    f"  Resource entry: {inferred['resource_entry']}\n\n"
                    "Confirm using this configuration first?\n"
                    "  1. Confirm, proceed to self-check\n"
                    "  2. I want to adjust the database list\n"
                    "  3. Reconfigure using institution name/preset"
                ),
                "data": {"inferred": inferred},
            }

        name = value

        ok, msg = validate_school_name(name)
        if not ok:
            return {"next": "retry", "prompt": f"{msg}. Please re-enter the resource link or institution name:"}

        # Check preset library
        preset = match_school(name)
        if preset:
            self.matched_preset = preset
            self.data["school_name"] = preset["name"]
            self.data["source"] = "preset"

            # Pre-fill preset config
            auth = preset.get("auth", {})
            self.data["auth_type"] = auth.get("type", "cas")
            self.data["sso_domain"] = auth.get("sso_domain", "")
            self.data["carsi_entry"] = auth.get("carsi_entry", "")
            self.data["libraries"] = preset.get("libraries", [])
            self.data["notes"] = preset.get("notes", "")

            self.state = "step4"
            return {
                "next": "step4",
                "prompt": (
                    f"Matched preset institution: {preset['name']}\n"
                    f"  Auth type: {auth.get('type', 'Unknown')}\n"
                    f"  SSO domain: {auth.get('sso_domain', 'Unknown')}\n"
                    f"  CARSI entry: {auth.get('carsi_entry', 'Not configured')}\n"
                    f"  Preset databases: {', '.join(preset.get('libraries', []))}\n\n"
                    "Confirm using the above configuration?\n"
                    "  1. Confirm, complete configuration directly\n"
                    "  2. I want to adjust the database list\n"
                    "  3. This is not my institution, re-enter"
                ),
                "data": {"matched": preset["name"]},
            }

        # Not matched, enter manual fill
        self.data["school_name"] = name
        self.data["source"] = "manual"
        self.state = "step2"
        return {
            "next": "step2",
            "prompt": (
                f"'{name}' not found in presets, entering manual configuration wizard.\n\n"
                "Step 2: Is your institution connected to CARSI federation authentication?\n"
                "(CARSI is the unified identity authentication federation for universities, lookup: https://www.carsi.edu.cn/)\n\n"
                "  1. Yes, connected to CARSI\n"
                "  2. No / unsure, use library remote access (EZproxy)\n"
                "  3. Neither, I use VPN to connect to campus network"
            ),
        }

    # ===== Step 2: CARSI check =====
    def handle_step2(self, user_input: str) -> dict[str, Any]:
        """Process CARSI selection."""
        choice = user_input.strip()
        if choice == "1":
            self.data["use_carsi"] = True
            self.state = "step2b"
            return {
                "next": "step2b",
                "prompt": (
                    "Please paste your institution's CARSI entry URL.\n"
                    "(Found in member list at https://www.carsi.edu.cn/, "
                    "usually in the form https://xxx.edu.cn/idp/shibboleth)\n\n"
                    "If you cannot find it, enter 'skip' to leave blank and add later."
                ),
            }
        elif choice == "2":
            self.data["use_carsi"] = False
            self.state = "step3"
            return {
                "next": "step3",
                "prompt": (
                    "You selected library remote access (EZproxy).\n\n"
                    "Step 3: Please enter your institution's unified authentication domain.\n"
                    "(Usually in the form id.xxx.edu.cn / cas.xxx.edu.cn / sso.xxx.edu.cn, "
                    "for example id.tsinghua.edu.cn)"
                ),
            }
        elif choice == "3":
            self.data["use_carsi"] = False
            self.data["use_vpn"] = True
            self.state = "step3"
            return {
                "next": "step3",
                "prompt": (
                    "Okay, using VPN mode.\n"
                    "Please ensure you are connected to campus VPN, then enter your institution's unified authentication domain.\n"
                    "(Usually in the form id.xxx.edu.cn / cas.xxx.edu.cn)"
                ),
            }
        return {"next": "retry", "prompt": "Please enter 1, 2, or 3:"}

    # ===== Step 2b: CARSI entry URL =====
    def handle_step2b(self, user_input: str) -> dict[str, Any]:
        """Process CARSI entry URL input."""
        url = user_input.strip()
        if url in ("skip", ""):
            self.data["carsi_entry"] = ""
            self.state = "step3"
            return {
                "next": "step3",
                "prompt": (
                    "CARSI entry skipped (can be added later).\n\n"
                    "Step 3: Please enter your institution's unified authentication domain.\n"
                    "(Usually in the form id.xxx.edu.cn / cas.xxx.edu.cn / sso.xxx.edu.cn)"
                ),
            }

        # Validation
        ok, msg = validate_carsi_entry(url)
        if not ok:
            return {
                "next": "retry",
                "prompt": f"{msg}\n\nPlease re-enter CARSI entry URL, or enter 'skip' to leave blank:",
            }

        self.data["carsi_entry"] = url
        self.state = "step3"
        return {
            "next": "step3",
            "prompt": (
                f"CARSI entry validated.\n\n"
                "Step 3: Please enter your institution's unified authentication domain.\n"
                "(Usually in the form id.xxx.edu.cn / cas.xxx.edu.cn / sso.xxx.edu.cn)"
            ),
        }

    # ===== Step 3: SSO domain =====
    def handle_step3(self, user_input: str) -> dict[str, Any]:
        """Process SSO domain input."""
        domain = user_input.strip()
        if not domain:
            return {"next": "retry", "prompt": "Domain cannot be empty, please re-enter:"}

        ok, msg = validate_sso_domain(domain)
        if not ok:
            return {
                "next": "retry",
                "prompt": f"{msg}\n\nPlease re-enter SSO domain (e.g. id.xxx.edu.cn):",
            }

        self.data["sso_domain"] = domain.split("://")[-1].split("/")[0]
        # If auth_type not set, default to cas
        if "auth_type" not in self.data:
            self.data["auth_type"] = "cas"

        # If using EZproxy path
        if not self.data.get("use_carsi", True) and not self.data.get("use_vpn"):
            self.state = "step5"
            return {
                "next": "step5",
                "prompt": (
                    f"SSO domain validated: {msg}\n\n"
                    "Step 5: Please enter your institution library's EZproxy login address.\n"
                    "(Tip: Using EZproxy usually requires enabling 'remote access' permissions on the library website first)\n\n"
                    "If unsure, enter 'skip' to add later."
                ),
            }

        self.state = "step4"
        return {
            "next": "step4",
            "prompt": (
                f"SSO domain validated: {msg}\n\n"
                "Step 4: What databases do you frequently download from?\n"
                f"Options: {', '.join(KNOWN_DATABASES[:10])} ...\n\n"
                "Please enter database names, separated by commas or spaces:"
            ),
        }

    # ===== Step 4: Database multi-select =====
    def handle_step4(self, user_input: str) -> dict[str, Any]:
        """Process database selection."""
        if user_input.strip().lower() in ("confirm", "1", "ok", "yes"):
            # Preset confirmation flow
            if not self.data.get("libraries"):
                return {"next": "retry", "prompt": "Please enter database names:"}
        else:
            # Parse input
            libs = [s.strip() for s in user_input.replace(",", " ").split() if s.strip()]
            if libs:
                self.data["libraries"] = libs

        ok, msg = validate_libraries(self.data.get("libraries", []))
        if not ok:
            return {"next": "retry", "prompt": f"{msg}. Please re-enter:"}

        self.state = "step6"
        return {
            "next": "step6",
            "prompt": (
                f"Recorded {len(self.data['libraries'])} databases.\n\n"
                "Step 6: Performing connectivity self-check..."
            ),
        }

    # ===== Step 5: EZproxy address =====
    def handle_step5(self, user_input: str) -> dict[str, Any]:
        """Process EZproxy address input."""
        url = user_input.strip()
        if url in ("skip", ""):
            self.data["ezproxy_url"] = None
            self.state = "step4"
            return {
                "next": "step4",
                "prompt": (
                    "EZproxy skipped.\n\n"
                    "Step 4: What databases do you frequently download from?\n"
                    "Please enter database names, separated by commas or spaces:"
                ),
            }

        ok, msg = validate_ezproxy_url(url)
        if not ok:
            return {
                "next": "retry",
                "prompt": f"{msg}\n\nPlease re-enter EZproxy address, or enter 'skip':",
            }

        self.data["ezproxy_url"] = url
        self.state = "step4"
        return {
            "next": "step4",
            "prompt": (
                f"EZproxy validated: {msg}\n\n"
                "Step 4: What databases do you frequently download from?\n"
                "Please enter database names, separated by commas or spaces:"
            ),
        }

    # ===== Step 6: Connectivity self-check =====
    def handle_step6(self, user_input: str = "") -> dict[str, Any]:
        """Execute connectivity self-check."""
        # Lazy import to avoid circular dependency
        from health_check import health_check, clear_cache

        # Save temporary config before check
        try:
            temp_config = self._build_config()
        except ValueError as e:
            return {"next": "retry", "prompt": f"Configuration build failed: {e}"}

        # Save temporarily for self-check
        clear_cache()
        save_config(temp_config)
        result = health_check(force=True)

        self.state = "step7"
        details_text = "\n".join(f"  {d}" for d in result.get("details", []))
        if result["ok"]:
            return {
                "next": "step7",
                "prompt": (
                    f"Connectivity self-check passed:\n{details_text}\n\n"
                    "Step 7: Confirm saving configuration?\n  1. Confirm save\n  2. Reconfigure"
                ),
            }
        else:
            suggestions = "\n".join(f"  {s}" for s in result.get("suggestions", []))
            return {
                "next": "step7",
                "prompt": (
                    f"Connectivity self-check completed with warnings:\n{details_text}\n\n"
                    f"{suggestions}\n\n"
                    "Step 7: How to proceed?\n"
                    "  1. Save anyway (can fix later)\n"
                    "  2. Reconfigure"
                ),
                "data": {"warnings": result.get("details", [])},
            }

    # ===== Step 7: Persistence =====
    def handle_step7(self, user_input: str) -> dict[str, Any]:
        """Process final save confirmation."""
        choice = user_input.strip().lower()
        if choice in ("2", "reconfigure", "redo", "reset"):
            delete_config()
            self.__init__()
            return {"next": "step1", "prompt": self.start()}

        # Save
        try:
            config = self._build_config()
            # Attach warnings (if any)
            if self.data.get("warnings"):
                config["_warnings"] = self.data["warnings"]
            path = save_config(config)
            return {
                "next": "done",
                "prompt": (
                    f"Configuration completed for '{self.data['school_name']}'!\n"
                    f"Config file: {path}\n\n"
                    "You can now download literature directly. To switch institutions anytime, ask to 'reconfigure' or use /reconfig."
                ),
                "data": {"school": self.data["school_name"], "path": str(path)},
            }
        except ValueError as e:
            return {"next": "retry", "prompt": f"Save failed: {e}\nPlease check and try again:"}

    # ===== Dispatch entry point =====
    def handle(self, user_input: str) -> dict[str, Any]:
        """Dispatch to corresponding handler based on current state."""
        handlers = {
            "step1": self.handle_step1,
            "step2": self.handle_step2,
            "step2b": self.handle_step2b,
            "step3": self.handle_step3,
            "step4": self.handle_step4,
            "step5": self.handle_step5,
            "step6": self.handle_step6,
            "step7": self.handle_step7,
        }
        handler = handlers.get(self.state)
        if handler is None:
            self.state = "step1"
            return {"next": "step1", "prompt": self.start()}
        return handler(user_input)

    # ===== Non-interactive: Preset school one-click configuration =====
    def configure_from_preset(self, school_name: str) -> dict[str, Any]:
        """One-click configuration from preset (non-interactive).

        Returns saved config dict on success, raises ValueError on failure.
        """
        preset = match_school(school_name)
        if not preset:
            raise ValueError(f"'{school_name}' not found in preset library")

        auth = preset.get("auth", {})
        config = {
            "version": 1,
            "school": {
                "name": preset["name"],
                "code": preset.get("aliases", [""])[0] if preset.get("aliases") else None,
                "configured_at": datetime.now().isoformat(),
                "source": "preset",
            },
            "auth": {
                "type": auth.get("type", "cas"),
                "sso_domain": auth.get("sso_domain", ""),
                "carsi_entry": auth.get("carsi_entry") or None,
                "carsi_sp_entity_id": None,
            },
            "proxy": {
                "type": None,
                "ezproxy_url": None,
            },
            "libraries": preset.get("libraries", []),
            "discovery": preset.get("discovery", {}),
            "notes": preset.get("notes", ""),
        }

        path = save_config(config)
        return {"config": config, "path": str(path)}

    # ===== Non-interactive: Resource URL configuration =====
    def configure_from_resource_url(self, resource_url: str) -> dict[str, Any]:
        """Configure from a library resource portal or authentication URL."""
        inferred = infer_access_from_url(resource_url)
        self.data.update(inferred)
        self.data["school_name"] = inferred.get("institution_hint") or inferred["entry_host"]
        self.data["source"] = "resource_url"
        self.data["auth_type"] = inferred["auth_type"]
        self.data["sso_domain"] = inferred["sso_domain"]
        self.data["carsi_entry"] = inferred["resource_entry"]
        self.data["libraries"] = ["Web of Science", "ScienceDirect", "Springer", "IEEE Xplore", "CNKI", "ACS"]
        self.data["notes"] = inferred.get("notes", "")
        self.data["discovery"] = {"resource_entry_url": inferred["resource_entry"]}
        if inferred["entry_type"] == "resource_portal":
            self.data["discovery"]["resource_portal_url"] = inferred["resource_entry"]
        if inferred.get("service_host"):
            self.data["discovery"]["auth_service_host"] = inferred["service_host"]

        config = self._build_config()
        path = save_config(config)
        return {"config": config, "path": str(path), "inferred": inferred}

    # ===== Internal: Build config dictionary =====
    def _build_config(self) -> dict[str, Any]:
        """Build configuration dictionary from data collected in wizard."""
        if not self.data.get("school_name"):
            raise ValueError("Institution name not set")
        if not self.data.get("sso_domain"):
            raise ValueError("SSO domain not set")
        if not self.data.get("libraries"):
            raise ValueError("Database list not set")

        return {
            "version": 1,
            "school": {
                "name": self.data["school_name"],
                "code": None,
                "configured_at": datetime.now().isoformat(),
                "source": self.data.get("source", "manual"),
            },
            "auth": {
                "type": self.data.get("auth_type", "cas"),
                "sso_domain": self.data["sso_domain"],
                "carsi_entry": self.data.get("carsi_entry") or None,
                "carsi_sp_entity_id": None,
            },
            "proxy": {
                "type": "ezproxy" if self.data.get("ezproxy_url") else None,
                "ezproxy_url": self.data.get("ezproxy_url") or None,
            },
            "libraries": self.data["libraries"],
            "discovery": self.data.get("discovery", {}),
            "notes": self.data.get("notes", ""),
        }


if __name__ == "__main__":
    # Non-interactive one-click configuration example
    w = Wizard()
    try:
        result = w.configure_from_preset("SJTU")
        print(f"Configured successfully: {result['config']['school']['name']}")
        print(f"Config file: {result['path']}")
    except ValueError as e:
        print(f"Configuration failed: {e}")
        print(f"Config file path: {CONFIG_FILE}")
