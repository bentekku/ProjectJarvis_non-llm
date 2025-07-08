import os
import uuid
from edge_tts import Communicate
from playsound import playsound

VOICE = "en-GB-RyanNeural"
RATE = "+0%"  # You can tweak this to '+10%' or '-10%'


async def _speak_async(text: str, voice: str = VOICE, rate: str = RATE):
    """
    Internal async function that uses edge-tts to generate speech and play it.
    """
    try:
        # Unique filename to avoid conflicts
        filename = f"temp_{uuid.uuid4()}.mp3"

        # Generate MP3 with edge-tts
        communicate = Communicate(text, voice=voice, rate=rate)
        await communicate.save(filename)

        # Play the MP3
        playsound(filename)

        # Clean up
        os.remove(filename)
    except Exception as e:
        print(f"[TTS ERROR] {e}")
