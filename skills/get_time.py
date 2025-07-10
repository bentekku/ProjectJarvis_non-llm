from modules.basic_tasks import get_time

TRIGGER_WORDS = ["time", "what's the time", "what time is it?"]


def can_handle(command: str) -> str:
    return any(phrase in command.lower() for phrase in TRIGGER_WORDS)


def handle(command: str) -> str:
    return get_time()
