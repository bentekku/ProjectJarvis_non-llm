import json
from pathlib import Path

LINKS_FILE = Path("data") / "links.json"


def get_link(name: str) -> str | None:
    if LINKS_FILE.exists():
        with open(LINKS_FILE, "r") as f:
            links = json.load(f)
            return links.get(name.lower())
    return None
