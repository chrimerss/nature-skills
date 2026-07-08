"""Field validation module.

Performs real-time reachability checks on user-configured fields:
- sso_domain: DNS resolution + TCP 443 + HTTPS certificate
- carsi_entry: HTTP GET check
- ezproxy_url: HTTP GET check for login form

All validation functions return (ok: bool, message: str).
"""

from __future__ import annotations

import socket
import ssl
import urllib.parse
import urllib.request


def validate_sso_domain(domain: str, timeout: float = 5.0) -> tuple[bool, str]:
    """Validate SSO domain: DNS resolution + TCP 443 + HTTPS certificate.

    Returns (is_valid, message).
    """
    domain = domain.strip().lower()
    if not domain:
        return False, "Domain is empty"

    # Remove protocol prefix
    for prefix in ("https://", "http://"):
        if domain.startswith(prefix):
            domain = domain[len(prefix):]
    domain = domain.split("/")[0]

    # DNS resolution
    try:
        addrs = socket.getaddrinfo(domain, 443, socket.AF_UNSPEC, socket.SOCK_STREAM)
    except socket.gaierror:
        return False, f"DNS resolution failed: {domain}, please check domain spelling"

    # TCP 443 connection + TLS handshake
    last_err = ""
    for family, socktype, proto, _, sockaddr in addrs:
        try:
            with socket.create_connection(sockaddr, timeout=timeout) as sock:
                ctx = ssl.create_default_context()
                with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    if cert is None:
                        return False, f"HTTPS certificate invalid: {domain}"
            return True, f"SSO domain reachable: https://{domain}"
        except (socket.timeout, ConnectionRefusedError, OSError) as e:
            last_err = str(e)
            continue

    return False, f"Cannot connect to https://{domain} (port 443): {last_err}"


def validate_carsi_entry(url: str, timeout: float = 8.0) -> tuple[bool, str]:
    """Validate CARSI entry: HTTP GET check.

    Criteria: returns 2xx/3xx, and page content contains 'CARSI', 'Shibboleth', or SSO redirect characteristics.
    """
    url = url.strip()
    if not url:
        return False, "CARSI entry URL is empty"

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (lit-dl-config-validator)",
                "Accept": "text/html",
            },
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.getcode()
            body = resp.read(4096).decode("utf-8", errors="ignore").lower()

            if status >= 400:
                return False, f"CARSI entry returned HTTP {status}"

            # Content feature check
            keywords = ["carsi", "shibboleth", "idp", "sso", "login"]
            matched = [k for k in keywords if k in body]
            if matched:
                return True, f"CARSI entry reachable, detected features: {', '.join(matched[:3])}"

            # 3xx redirect also passes (may redirect to SSO)
            if 300 <= status < 400:
                location = resp.headers.get("Location", "")
                return True, f"CARSI entry redirects to: {location}"

            return True, f"CARSI entry reachable (HTTP {status}), but no obvious SSO features detected"

    except urllib.error.URLError as e:
        return False, f"CARSI entry unreachable: {e.reason}"
    except Exception as e:
        return False, f"CARSI entry check exception: {e}"


def validate_ezproxy_url(url: str, timeout: float = 8.0) -> tuple[bool, str]:
    """Validate EZproxy address: HTTP GET check for login form.

    Criteria: page contains password input field.
    """
    url = url.strip()
    if not url:
        return False, "EZproxy URL is empty"

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (lit-dl-config-validator)",
                "Accept": "text/html",
            },
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.getcode()
            body = resp.read(8192).decode("utf-8", errors="ignore").lower()

            if status >= 400:
                return False, f"EZproxy returned HTTP {status}"

            if "password" in body or "passwd" in body:
                return True, "EZproxy login page reachable, detected password input field"

            return True, f"EZproxy page reachable (HTTP {status}), but login form not detected"

    except urllib.error.URLError as e:
        return False, f"EZproxy unreachable: {e.reason}"
    except Exception as e:
        return False, f"EZproxy check exception: {e}"


def validate_school_name(name: str) -> tuple[bool, str]:
    """Validate institution name basic format."""
    name = name.strip()
    if len(name) < 2:
        return False, "Institution name too short"
    if len(name) > 100:
        return False, "Institution name too long"
    return True, name


def validate_libraries(libraries: list[str]) -> tuple[bool, str]:
    """Validate database list."""
    if not libraries:
        return False, "Database list cannot be empty"
    if len(libraries) > 50:
        return False, "Database list too long"
    return True, f"Selected {len(libraries)} databases"


# Known database list (for wizard multi-select hints)
KNOWN_DATABASES = [
    "CNKI",
    "Wanfang",
    "VIP",
    "Web of Science",
    "Scopus",
    "IEEE Xplore",
    "ScienceDirect",
    "Springer Link",
    "Wiley Online Library",
    "ACS Publications",
    "RSC Publishing",
    "Nature",
    "Science",
    "Elsevier ScienceDirect",
    "Taylor & Francis",
    "SAGE Journals",
    "EBSCO",
    "ProQuest",
    "JSTOR",
    "PubMed",
]


if __name__ == "__main__":
    # Self-check example
    print("=== SSO Domain Validation ===")
    ok, msg = validate_sso_domain("jaccount.sjtu.edu.cn")
    print(f"  {ok}: {msg}")

    print("\n=== CARSI Entry Validation ===")
    ok, msg = validate_carsi_entry("https://www.carsi.edu.cn/")
    print(f"  {ok}: {msg}")
