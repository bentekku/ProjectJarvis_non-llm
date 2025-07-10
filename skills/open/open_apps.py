import subprocess
from utils.app_utils import get_known_apps

TRIGGER_WORDS = ["open", "fire up", "pull up", "launch"]


def can_handle(command: str) -> str:
    return any(phrase in command.lower() for phrase in TRIGGER_WORDS)


def handle(command: str) -> str:

    cleaned = cleaned_app_name(command)
    apps = get_known_apps()

    if cleaned in apps:
        try:
            subprocess.Popen(str(apps[cleaned]))  # always convert to string
            return f"Opening {cleaned}, boss."
        except Exception as e:
            print(f"[Jarvis Error] Failed to open {cleaned}: {e}")
            return f"Failed to open {cleaned}, boss."
    if cleaned not in apps:
        print(f"[Jarvis]: Registered known apps → {list(apps)}")
        return f"{cleaned} is not configured yet, boss. Want me to learn it next time?"


def cleaned_app_name(text: str) -> str:
    text = text.lower()
    for trigger in TRIGGER_WORDS:
        if text.startswith(trigger):
            return text.replace(trigger, "").strip()
    return text
