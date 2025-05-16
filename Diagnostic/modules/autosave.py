import os, json
from modules.utils import get_scan_folder

MAX_SAVES = 5

def save_scan(data):
    path = get_scan_folder()
    files = sorted(os.listdir(path))
    # prune old
    while len(files) >= MAX_SAVES:
        os.remove(os.path.join(path, files.pop(0)))
    fname = f"scan_{data['timestamp'].replace(':','-')}.json"
    with open(os.path.join(path, fname), 'w') as f:
        json.dump(data, f, indent=2)


def load_scans():
    path = get_scan_folder()
    scans = []
    for fn in sorted(os.listdir(path)):
        with open(os.path.join(path, fn)) as f:
            scans.append(json.load(f))
    return scans