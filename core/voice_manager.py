import os
import shutil
import uuid
from edge_tts import Communicate
from playsound import playsound
import pathlib

VOICE = "en-GB-RyanNeural"
DEFAULT_RATE = "+0%"
DEFAULT_PITCH = "+0Hz"

# Mood -> Voice modulation wrapper mappings
MOOD_SETTINGS = {
    "default": {"pitch": "+0Hz", "rate": "+0%"},
    "happy": {"pitch": "+4Hz", "rate": "+5%"},
    "intense": {"pitch": "-10Hz", "rate": "+5%"},
    "sarcastic": {"pitch": "-5Hz", "rate": "+5%"},  # subtle tone shift
    "alert": {"pitch": "+15Hz", "rate": "+20%"},
    "calm": {"pitch": "-5Hz", "rate": "-5%"},
}


async def _speak_async(text: str, mood: str = "sarcastic"):
    """
    Internal async function that uses edge-tts to generate speech and play it.
    Uses edge-tts with pitch and rate parameters to speak text with mood modulation.
    """

    try:
        # Get pitch and rate for the mood, default if mood unknown
        settings = MOOD_SETTINGS.get(
            mood, MOOD_SETTINGS["sarcastic"]
        )  # sarcastic sounds better than the rest of them

        # Make sure folder exists
        temp_folder = pathlib.Path("___temp/voice")
        temp_folder.mkdir(parents=True, exist_ok=True)
        # Unique filename to avoid conflicts
        filename = temp_folder / f"temp_{uuid.uuid4()}.mp3"

        # Generate MP3 with edge-tts
        communicate = Communicate(
            text=text, voice=VOICE, pitch=settings["pitch"], rate=settings["rate"]
        )
        await communicate.save(str(filename))

        # Play the MP3
        playsound(str(filename))

        # Clean up
        os.remove(str(filename))
    except Exception as e:
        print(f"[TTS ERROR] {e}")


def cleanup_temp_folder():
    try:
        temp_root = pathlib.Path("___temp")
        if temp_root.exists():
            shutil.rmtree(temp_root)
            print("[Jarvis] Temporary files cleaned up, boss.")
    except Exception as e:
        print(f"[Jarvis Cleanup Error]: {e}")
