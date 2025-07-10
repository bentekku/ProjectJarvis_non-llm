import webbrowser
import json
from pathlib import Path
from utils.link_manager import get_link
from utils.path_utils import LINKS_FILE


TRIGGER_WORDS = ["open", "fire up", "pull up", "launch"]

with open(LINKS_FILE, "r", encoding="utf-8") as f:
    LINKS = json.load(f)


def can_handle(command: str) -> bool:
    if any(phrase in command.lower() for phrase in TRIGGER_WORDS):
        for TRIGGER in TRIGGER_WORDS:
            if TRIGGER:
                text = command.lower().replace(TRIGGER, "")
                return any(link in text for link in LINKS)


def handle(command: str) -> str:
    command = command.lower()
    url = get_link(command)
    if url:
        webbrowser.open(url)
        return f"Firing up your {command}, boss."
    else:
        return f"I couldn't find link for {command}, boss."
