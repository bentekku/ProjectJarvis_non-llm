import speech_recognition as sr
import asyncio
from core.voice_manager import _speak_async


def speak(text: str):
    """
    Public function to speak text aloud using edge-tts.
    """
    asyncio.run(_speak_async(text))


def listen() -> str:
    """
    Listen to microphone input and return recognized speech as text.
    Returns empty string if speech is unintelligible or service unavailable.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis: Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Speech service is unavailable.")
        speak("Speech service is unavailable.")
        return ""
