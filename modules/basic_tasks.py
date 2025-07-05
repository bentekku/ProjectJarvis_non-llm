import os
import subprocess
from pathlib import Path
from datetime import datetime
from utils.folder_utils import FOLDERS
from utils.app_utils import APPS

def get_time() -> str:
    now = datetime.now()
    return now.strftime("The time is %I:%M %p")

def get_date() -> str:
    now = datetime.now()
    return now.strftime("Today is %B %d, %Y")

def get_day_name() -> str:
    now = datetime.now()
    return now.strftime("It's %A today")

def get_day_number() -> str:
    now = datetime.now()
    return f"Today is day number {now.isoweekday()} of the week"

def open_app(app_name: str) -> str:
    """
    Opens a known application based on the given app name.
    """
    app_name = app_name.lower()

    if app_name in APPS:
        try:
            path = APPS[app_name]
            if not Path(path).exists():
                return f"{app_name} is not installed where I expected it, boss."
            subprocess.Popen(APPS[app_name]) # Launch the app
            return f"Opening {app_name}, boss"
        except Exception as e:
            print(f"Error: {e}")
            return f"Failed to open {app_name}."
    else:
        return f"Sorry boss, I don't know how to open {app_name} yet."
    
def open_folder(folder_name: str) -> str:
    """
    Opens a known user folder (like Downloads, Desktop, Documents).
    """
    folder_name = folder_name.lower()

    if folder_name in FOLDERS:
        try:
            os.startfile(FOLDERS[folder_name])
            return f"Opening your {folder_name} folder, boss."
        except Exception as e:
            print(f"Error: {e}")
            return f"Could not open {folder_name}."

    else:
        return f"I'm not familiar with the {folder_name} folder yet."
