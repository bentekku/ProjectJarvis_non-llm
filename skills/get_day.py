from modules.basic_tasks import get_day_name

TRIGGER_WORDS = ["what day is it", "what's the day"]


def can_handle(command: str) -> str:
    return any(phrase in command.lower() for phrase in TRIGGER_WORDS)


def handle(command: str) -> str:
    return get_day_name()
