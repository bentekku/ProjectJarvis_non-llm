from modules.basic_tasks import get_date

TRIGGER_WORDS = ["date", "what's the date", "what date is it"]


def can_handle(command: str) -> str:
    return any(phrase in command.lower() for phrase in TRIGGER_WORDS)


def handle(command: str) -> str:
    return get_date()
