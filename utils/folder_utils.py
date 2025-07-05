from pathlib import Path

def get_known_folders() -> list:
    """
    Returns a list of known folder names that Jarvis can open.
    """
    return list(FOLDERS.keys())

FOLDERS = {
    "desktop": str(Path.home() / "OneDrive" / "Desktop"),
    "documents": str(Path.home() / "OneDrive" / "Documents"),
    "pictures": str(Path.home() / "OneDrive" / "Pictures"),
    "downloads": str(Path.home() /  "Downloads"),
    "music": str(Path.home() / "Music"),
    "videos": str(Path.home() / "Videos")
}
