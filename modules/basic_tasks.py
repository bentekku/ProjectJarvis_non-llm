from pathlib import Path
from datetime import datetime


def get_time() -> str:
    now = datetime.now()
    return now.strftime("The time is %I:%M %p")


def get_date() -> str:
    now = datetime.now()
    return now.strftime("Today is %B %d, %Y")


def get_day_name() -> str:
    now = datetime.now()
    return now.strftime("It's %A today")


def get_day_number() -> str:
    now = datetime.now()
    return f"Today is day number {now.isoweekday()} of the week"
