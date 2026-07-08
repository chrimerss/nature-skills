"""Configuration read/write module.

Responsible for reading, writing, validating, and backing up school.json.
Config path: ~/.config/lit-dl/school.json
"""

from __future__ import annotations

import json
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

try:
    import jsonschema  # type: ignore
except ImportError:
    jsonschema = None  # type: ignore

# Config file path (supports environment variable override for testing and multiple profiles)
CONFIG_DIR = Path(os.environ.get("LIT_DL_CONFIG_DIR", Path.home() / ".config" / "lit-dl"))
CONFIG_FILE = CONFIG_DIR / "school.json"

# Schema path (relative to this file)
SCHEMA_FILE = Path(__file__).resolve().parent.parent / "data" / "school.schema.json"


def load_schema() -> dict[str, Any]:
    """Load JSON Schema."""
    with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def config_exists() -> bool:
    """Check if config file exists."""
    return CONFIG_FILE.exists()


def validate(config: dict[str, Any]) -> list[str]:
    """Validate whether config conforms to schema.

    Returns a list of error messages, empty list indicates success.
    If jsonschema is not installed, schema validation is skipped and only basic field checks are performed.
    """
    errors: list[str] = []

    # Basic field check (independent of jsonschema)
    if not isinstance(config, dict):
        return ["Configuration is not a valid JSON object"]
    if "version" not in config:
        errors.append("Missing version field")
    if "school" not in config or "name" not in config.get("school", {}):
        errors.append("Missing school.name field")
    auth = config.get("auth", {})
    if "type" not in auth:
        errors.append("Missing auth.type field")
    if "sso_domain" not in auth or not auth["sso_domain"]:
        errors.append("Missing auth.sso_domain field")
    if not config.get("libraries"):
        errors.append("libraries cannot be empty")

    # Schema validation (optional)
    if jsonschema is not None and not errors:
        try:
            jsonschema.validate(instance=config, schema=load_schema())
        except jsonschema.ValidationError as e:  # type: ignore
            errors.append(f"Schema validation failed: {e.message}")

    return errors


def load_config() -> Optional[dict[str, Any]]:
    """Read configuration file.

    Returns config dictionary, or None if file does not exist.
    If JSON parsing fails, automatically backs up the broken file and returns None.
    """
    if not CONFIG_FILE.exists():
        return None

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        # Config file corrupted, backup and return None
        backup = CONFIG_FILE.with_suffix(".json.broken")
        shutil.copy2(CONFIG_FILE, backup)
        try:
            CONFIG_FILE.unlink()
        except OSError:
            pass
        print(f"Config file corrupted, backed up to {backup}. Please reconfigure. Error: {e}")
        return None


def save_config(config: dict[str, Any]) -> Path:
    """Write configuration file.

    Automatically creates directories and adds configured_at timestamp.
    Returns config file path.
    """
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    # Add timestamp
    if not config.get("school", {}).get("configured_at"):
        config.setdefault("school", {})["configured_at"] = datetime.now().isoformat()

    # Validate
    errors = validate(config)
    if errors:
        raise ValueError(f"Configuration validation failed: {'; '.join(errors)}")

    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

    # Set file permissions (read/write by owner only)
    os.chmod(CONFIG_FILE, 0o600)

    return CONFIG_FILE


def backup_config() -> Optional[Path]:
    """Backup current configuration file, returns backup path. Returns None if file does not exist."""
    if not CONFIG_FILE.exists():
        return None
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = CONFIG_FILE.with_suffix(f".json.{timestamp}.bak")
    shutil.copy2(CONFIG_FILE, backup)
    return backup


def delete_config() -> bool:
    """Delete configuration file (for reconfiguration). Returns whether deletion was successful."""
    if CONFIG_FILE.exists():
        backup_config()
        CONFIG_FILE.unlink()
        return True
    return False


def get_school_name() -> Optional[str]:
    """Quickly get institution name. Returns None if not configured."""
    cfg = load_config()
    if cfg is None:
        return None
    return cfg.get("school", {}).get("name")


def get_auth_info() -> Optional[dict[str, Any]]:
    """Quickly get authentication info. Returns None if not configured."""
    cfg = load_config()
    if cfg is None:
        return None
    return cfg.get("auth")


if __name__ == "__main__":
    # CLI self-check
    if config_exists():
        cfg = load_config()
        if cfg:
            print(f"Configured institution: {cfg.get('school', {}).get('name', 'Unknown')}")
            print(f"Config path: {CONFIG_FILE}")
            errors = validate(cfg)
            if errors:
                print(f"Validation warnings: {errors}")
            else:
                print("Configuration validation passed")
        else:
            print("Config file exists but is corrupted, please reconfigure")
    else:
        print(f"Not configured yet, config path: {CONFIG_FILE}")
