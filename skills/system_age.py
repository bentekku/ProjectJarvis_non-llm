from utils.days_passed import calculate_days_passed

TRIGGER_WORDS = [
    "how old are you",
    "what's your age",
    "how long have you been online",
]


def can_handle(command: str) -> str:
    return any(phrase in command.lower() for phrase in TRIGGER_WORDS)


def handle(command: str) -> str:
    return calculate_days_passed()
