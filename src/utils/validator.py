from environments import mod_path
import os

def validate_path(path: str):
    full_path = mod_path / f"{path}"
    if os.path.isfile(full_path):
        return str(full_path)
    return path
