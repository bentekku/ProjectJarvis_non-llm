from pathlib import Path
import glob


def get_known_apps() -> list:
    """
    Returns a list of known folder names that Jarvis can open.
    """
    return list(APPS.keys())


# Auto-detect latest installed Discord version
def get_discord_path():
    discord_base = Path.home() / "AppData" / "Local" / "Discord"
    matches = glob.glob(str(discord_base / "app-*" / "Discord.exe"))

    # Returns first match or None
    return matches[0] if matches else None


# Build the dictionary with fallback for Discord
APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vs code": str(
        Path.home()
        / "AppData"
        / "Local"
        / "Programs"
        / "Microsoft VS Code"
        / "Code.exe"
    ),
    "notepad": "notepad",
    "calculator": "calc",
    "command prompt": "cmd",
    "explorer": "explorer",
    "spotify": Path.home() / "AppData" / "Roaming" / "Spotify" / "Spotify.exe",
}

# If Discord is found, add it to the APPS map
discord_path = get_discord_path()
if discord_path:
    APPS["discord"] = discord_path
