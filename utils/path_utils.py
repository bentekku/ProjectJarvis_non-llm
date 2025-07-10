from pathlib import Path

# Root directory of your ProjectJarvis repo
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Directory paths
DATA_DIR = PROJECT_ROOT / "data"
TEMP_DIR = PROJECT_ROOT / "temp"
VOICE_TEMP_DIR = TEMP_DIR / "voice"
SKILLS_DIR = PROJECT_ROOT / "skills"
UTILS_DIR = PROJECT_ROOT / "utils"

# File paths
RESPONSES_FILE = DATA_DIR / "jarvis_responses.json"
LINKS_FILE = DATA_DIR / "links.json"

# Exported constants
__all__ = [
    "PROJECT_ROOT",
    "DATA_DIR",
    "TEMP_DIR",
    "VOICE_TEMP_DIR",
    "SKILLS_DIR",
    "UTILS_DIR",
    "RESPONSES_FILE",
    "LINKS_FILE",
]
