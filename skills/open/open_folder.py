import os
from utils.folder_utils import get_known_folders

TRIGGER_WORDS = ["open", "fire up", "pull up", "launch"]


def can_handle(command: str) -> str:
    return any(phrase in command.lower() for phrase in TRIGGER_WORDS)


def handle(command: str) -> str:
    cleaned = clean_folder_name(command)
    folder_path = get_known_folders(cleaned)

    if folder_path:
        try:
            os.startfile(folder_path)
            return f"Opening {folder_path}"
        except Exception as e:
            return f"Couldn't open {folder_path} folder boss"
    else:
        return f"Sorry boss, I don't know how to open {folder_path}"


def clean_folder_name(text: str) -> str:
    text = text.lower()

    for TRIGGER in TRIGGER_WORDS:
        if text.startswith(TRIGGER):
            return text.replace(TRIGGER, "").strip()
    return text
