from pathlib import Path
import glob


def get_known_apps() -> dict:
    """
    Returns a list of known folder names that Jarvis can open.
    """
    # return list(APPS.keys())
    return APPS


# Auto-detect latest installed Discord version
def get_discord_path():  # No need to call this function explicitly, it is handled automatically
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
    #     "notepad": "notepad.exe" if os.name == 'nt' else "nano", # Windows: notepad.exe, Linux/macOS: nano (text editor)
    #     "calculator": "calc.exe" if os.name == 'nt' else "gnome-calculator", # Windows: calc.exe, Linux: gnome-calculator
    #     "browser": "start chrome" if os.name == 'nt' else "google-chrome", # Windows: start chrome, Linux: google-chrome
    #     "terminal": "cmd.exe" if os.name == 'nt' else "xterm", # Windows: cmd.exe, Linux: xterm
    #     "paint": "mspaint.exe" if os.name == 'nt' else "gimp", # Windows: mspaint.exe, Linux: gimp
    #     "files": "explorer.exe" if os.name == 'nt' else "nautilus" # Windows: explorer.exe, Linux: nautilus
}

# If Discord is found, add it to the APPS map
discord_path = get_discord_path()
if discord_path:
    APPS["discord"] = discord_path
