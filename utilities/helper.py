from pathlib import Path
import os

def delete_file(file_path: Path):
    if file_path.exists():
        os.remove(file_path)
        return True
    return False
