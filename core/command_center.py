from modules.basic_tasks import get_time, get_date, get_day_name, get_day_number

def handle_command(command: str) -> str:
    command = command.lower()

    if "time" in command:
        return get_time()
    elif "date" in command:
        return get_date()
    elif "day number" in command or "day of the week" in command:
        return get_day_number()
    elif "day" in command:
        return get_day_name()
    else:
        return "Sorry boss, I can only tell time, date, and day for now."
