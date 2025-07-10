from utils.response_manager import get_random_response

TRIGGER_WORDS = ["how are you", "how you holding up", "system status"]


def can_handle(command: str) -> str:
    return any(phrase in command.lower() for phrase in TRIGGER_WORDS)


def handle(command: str) -> str:
    return get_random_response("how_are_you")
