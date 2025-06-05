
import os
import hashlib
import json
import time

# === Configuration ===
WATCH_DIRECTORY = './watch_folder'  # Folder to monitor
HASH_STORE = 'file_hashes.json'     # File to store hashes
SLEEP_INTERVAL = 10                 # Seconds between checks

def calculate_file_hash(filepath):
    """Calculate SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"[ERROR] Could not hash {filepath}: {e}")
        return None

def load_hashes():
    """Load stored hashes from JSON file."""
    if not os.path.exists(HASH_STORE):
        return {}
    with open(HASH_STORE, 'r') as f:
        return json.load(f)

def save_hashes(hashes):
    """Save hashes to JSON file."""
    with open(HASH_STORE, 'w') as f:
        json.dump(hashes, f, indent=2)

def scan_directory():
    """Scan the directory and calculate hashes for all files."""
    current_hashes = {}
    for root, _, files in os.walk(WATCH_DIRECTORY):
        for name in files:
            filepath = os.path.join(root, name)
            file_hash = calculate_file_hash(filepath)
            if file_hash:
                relative_path = os.path.relpath(filepath, WATCH_DIRECTORY)
                current_hashes[relative_path] = file_hash
    return current_hashes

def compare_hashes(old_hashes, new_hashes):
    """Compare two hash dictionaries and report changes."""
    old_files = set(old_hashes.keys())
    new_files = set(new_hashes.keys())

    added = new_files - old_files
    removed = old_files - new_files
    modified = {f for f in old_files & new_files if old_hashes[f] != new_hashes[f]}

    if added or removed or modified:
        print("\n[CHANGE DETECTED]")
        if added:
            print("  Added:")
            for f in added:
                print(f"    + {f}")
        if removed:
            print("  Removed:")
            for f in removed:
                print(f"    - {f}")
        if modified:
            print("  Modified:")
            for f in modified:
                print(f"    * {f}")
    else:
        print("[NO CHANGES]")

def monitor():
    print(f"Monitoring directory: {WATCH_DIRECTORY}")
    if not os.path.exists(WATCH_DIRECTORY):
        print(f"Creating watch directory: {WATCH_DIRECTORY}")
        os.makedirs(WATCH_DIRECTORY)

    old_hashes = load_hashes()

    while True:
        new_hashes = scan_directory()
        compare_hashes(old_hashes, new_hashes)
        save_hashes(new_hashes)
        old_hashes = new_hashes
        time.sleep(SLEEP_INTERVAL)

if __name__ == '__main__':
    monitor()
