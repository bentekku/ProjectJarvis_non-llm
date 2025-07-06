import json
import random
from pathlib import Path

RESPONSES_FILE = Path("data") / "jarvis_responses.json"


def get_random_response(category: str) -> str:
    """
    Fetch a random response for the given category.

    Args:
        category (str): The key from the JSON (like "how_are_you")

    Returns:
        str: A randomly selected witty response. Falls back if file/category missing.
    """
    if RESPONSES_FILE.exists():
        with open(RESPONSES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

            # If category exists. return random choice from it
            if category in data:
                return random.choice(data[category])

    return "I'm operational, but your response file is missing or incomplete."
