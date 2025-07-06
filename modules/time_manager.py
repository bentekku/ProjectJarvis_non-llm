import time
import threading
import re
from voice.voice_io import speak


def parse_duration(command: str) -> int:
    """
    Parses a natural language command to extract duration in seconds.
    Supports minutes, seconds, or both.
    Example: 'Set a timer for 1 minute and 30 seconds'
    """
    minutes = 0
    seconds = 0

    # Match patterns like "12 minutes", "30 secs", "1 minute and 20 seconds"
    min_match = re.search(r"(\d+)\s*(minute|minutes|min)", command)
    sec_match = re.search(r"\d+s*(second|seconds|secs)", command)

    if min_match:
        minutes = int(min_match.group(1))
    if sec_match:
        seconds = int(sec_match.group(1))

    total_seconds = minutes * 60 + seconds
    return total_seconds


def set_timer(duration_seconds: int) -> None:
    """
    Sets a countdown timer in the background.
    """

    def timer_thread():
        m = duration_seconds // 60
        s = duration_seconds % 60
        speak(
            f"Timer started for {m} minute{'s' if m != 1 else ''} and {s} second{'s' if s != 1 else ''}."
        )
        time.sleep(duration_seconds)
        speak("Boss, your timer is up.")

    threading.Thread(target=timer_thread, daemon=True).start()
