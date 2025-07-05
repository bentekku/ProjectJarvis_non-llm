from modules.basic_tasks import get_time, get_date, get_day_name, get_day_number, open_app, open_folder
from utils.folder_utils import get_known_folders

def handle_command(command: str) -> str:
    command = command.lower()

    if "time" in command:
        return get_time()
    elif "date" in command:
        return get_date()
    elif "day number" in command or "day of the week" in command:
        return get_day_number()
    elif "day" in command:
        return get_day_name()
    elif "open" in command:
        words = command.split("open", 1)[-1].strip()
        # Decide whether it's an app or folder
        if any(folder in words for folder in get_known_folders()):
            return open_folder(words)
        else:
            return open_app(words)
    else:
        return "Sorry boss, I can only tell time, date, day and opening things for now."
