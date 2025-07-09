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
from utils.days_passed import calculate_days_passed, boot_date


def handle_command(command: str) -> str:
    command = command.lower().strip()

    # 🧠 Basic conversations
    if any(
        phrase in command
        for phrase in ["how are you", "how you holding up", "system status"]
    ):
        return get_random_response("how_are_you")

    # ⏱ Timer
    if "timer" in command:
        return handle_timer(command)

    # 🗓️ Time & Date
    if "time" in command:
        return get_time()
    if "date" in command:
        return get_date()
    if "day number" in command:
        return get_day_number()
    if "day" in command:
        return get_day_name()

    # 🧭 App & Folder
    if command.startswith("open"):
        return handle_open(command)

    # 🎶 Custom link
    if any(phrase in command for phrase in ["play some funk", "fire up funk music"]):
        return open_link("phonk-playlist")

    # 🌐 Wiki Search
    if command.startswith(("who is", "what is", "define")):
        return handle_wiki(command)

    # 🔍 Google Search
    if "search google for" in command:
        topic = command.replace("search google for", "").strip()
        return google_search(topic)

    # 🔎 Web Scrape
    if "loop up" in command:
        topic = command.replace("look up", "").strip()
        return web_scrape_snippet(topic)

    # 🧮 System Age
    if any(
        phrase in command
        for phrase in [
            "how old are you",
            "what's your age",
            "how long have you been online",
        ]
    ):
        return calculate_days_passed()

    # 📅 Initialization Date
    if any(
        phrase in command
        for phrase in [
            "when were you first booted",
            "when were you born",
            "what's your boot date",
            "when did you go online",
        ]
    ):
        return boot_date()

    # 🤷‍♂️ Default
    return "Sorry boss, currently I'm operating at a fraction of full capacity."


# -------------------------------------------
# 💥 Subcommand Handlers
# -------------------------------------------


def handle_timer(command: str) -> str:
    try:
        seconds = parse_duration(command)
        if seconds > 0:
            set_timer(seconds)
            return "Timer set boss. You'll will be notified."
        return "I couldn't understand how long to set the timer for."
    except Exception as e:
        return f"Something went wrong while setting the timer: {str(e)}"


def handle_open(command: str) -> str:
    words = command.split("open", 1)[-1].strip()
    if any(folder in words for folder in get_known_folders):
        return open_folder(words)
    return open_app(words)


def handle_wiki(command: str) -> str:
    for prefix in ["who is", "what is", "define"]:
        if command.startswith(prefix):
            topic = command.replace(prefix)
            return search_wikipedia(topic)
        return "Sorry boss, I couldn't figure out what to look up on Wikipedia."
