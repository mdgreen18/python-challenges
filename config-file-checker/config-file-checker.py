import json
import shutil
from datetime import datetime

DEFAULT_CONFIG = {
    "api_key": "DEFAULT_KEY",
    "timeout": 60,
    "debug": False
}

def validate_and_update_config(file_path):
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"Config file not found: {file_path}")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return

    # Backup original
    backup_path = file_path + ".bak"
    shutil.copy(file_path, backup_path)
    print(f"Backup created at {backup_path}")

    updated = False
    for key, default in DEFAULT_CONFIG.items():
        if key not in config or not isinstance(config[key], type(default)):
            print(f"Missing or invalid key: {key}. Setting default: {default}")
            config[key] = default
            updated = True

    if updated:
        with open(file_path, 'w') as f:
            json.dump(config, f, indent=4)
        print("Updated config file saved.")
    else:
        print("No changes needed. Config is valid.")

if __name__ == "__main__":
    path = input("Enter path to the config file: ")
    validate_and_update_config(path)

