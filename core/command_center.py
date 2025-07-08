from modules.basic_tasks import (
    get_time,
    get_date,
    get_day_name,
    get_day_number,
    open_app,
    open_folder,
    open_link,
)
from modules.time_manager import parse_duration, set_timer
from modules.internet import search_wikipedia, google_search, web_scrape_snippet
from utils.folder_utils import get_known_folders
from utils.response_manager import get_random_response


def handle_command(command: str) -> str:
    command = command.lower()

    if "how are you" in command or "system status" in command:
        return get_random_response("how_are_you")
    elif "timer" in command:
        try:
            seconds = parse_duration(command)
            if seconds > 0:
                set_timer(seconds)
                return "Timer set, boss. You'll be notified."
            else:
                return "I couldn't understand how long to set the timer for, boss."
        except Exception as e:
            return f"Something went wrong while setting the timer: {str(e)}"
    elif "time" in command:
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
    elif "play some funk" in command or "fire up funk music" in command:
        # speak(f"Which one would you like me to play, Mr. Khan?")
        # if command
        return open_link("phonk-playlist")
    elif (
        command.startswith("who is")
        or command.startswith("what is")
        or command.startswith("define")
    ):
        topic = (
            command.replace("who is", "")
            or command.replace("what is", "")
            or command.replace("define", "").strip()
        )
        return search_wikipedia(topic)
    elif "search google for" in command:
        topic = command.replace("search google for", "").strip()
        return google_search(topic)
    elif "look up" in command or "search online" in command:
        topic = (
            command.replace("look up", "")
            or command.replace("search online", "").strip()
        )
        return web_scrape_snippet(topic)
    else:
        return "Sorry boss, currently I'm at operating at a fraction of full capacity."
