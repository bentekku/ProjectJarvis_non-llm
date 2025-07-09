import datetime
import json
from pathlib import Path

RESPONSE_FILE = Path("data") / "data.json"


def grab_init_date() -> str | None:
    if RESPONSE_FILE.exists():
        try:
            with open(RESPONSE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                init_date_str = data.get("initialization-date")
                return init_date_str
        except Exception as e:
            print(f"[Jarvis Error]: {e}")
            return None
    else:
        print("[Jarvis]: Your response file is missing.")
        return (
            "My memory is a bit hazy... can't seem to recall the exact number of days."
        )


def calculate_days_passed() -> str:
    init_date_str = grab_init_date()
    if init_date_str is not None:
        # Parse string to date
        init_date = datetime.datetime.strptime(init_date_str, "%Y-%m-%d").date()
        today = datetime.date.today()
        days_passed = (today - init_date).days
        return f"I’ve been online for {days_passed} days."
    else:
        return "My initialization date is missing, sir."


def boot_date() -> str:
    init_date_str = grab_init_date()
    if init_date_str is not None:
        # Parse string to date
        init_date = datetime.datetime.strptime(init_date_str, "%Y-%m-%d").date()
        return f"I was initialized for the first time on {init_date}."
    else:
        return "My initialization date is missing, sir."
