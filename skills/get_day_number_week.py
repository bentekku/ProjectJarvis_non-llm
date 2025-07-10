from modules.basic_tasks import get_day_number

TRIGGER_WORDS = ["what's the day number", "day number"]


def can_handle(command: str) -> str:
    return any(phrase in command.lower() for phrase in TRIGGER_WORDS)


def handle(command: str) -> str:
    return get_day_number()
