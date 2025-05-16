import os
from pathlib import Path


def get_scan_folder():
    return Path(os.getenv('APPDATA') or '.') / 'DiagnosisTool' / 'scans'


def ensure_scan_folder():
    folder = get_scan_folder()
    folder.mkdir(parents=True, exist_ok=True)