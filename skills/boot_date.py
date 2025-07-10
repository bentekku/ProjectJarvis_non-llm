from utils.days_passed import boot_date

TRIGGER_WORDS = [
    "when were you first booted",
    "when were you born",
    "what's your boot date",
    "when did you go online",
]


def can_handle(command: str) -> str:
    return any(phrase in command.lower() for phrase in TRIGGER_WORDS)


def handle(command: str) -> str:
    return boot_date()
