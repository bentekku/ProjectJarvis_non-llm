import speech_recognition as sr
import asyncio
from core.voice_manager import _speak_async


def speak(text: str, mood: str = "default"):
    """
    Speak text using pitch and rate modulation and edge-tts.
    mood: default | happy | intense | sarcastic | alert | calm
    """
    asyncio.run(_speak_async(text, mood))


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


# Bonus: a simple personality injector that picks mood based on keywords
# def choose_mood(text: str) -> str:
#     lowered = text.lower()
#     if any(word in lowered for word in ["great", "fantastic", "awesome", "cool"]):
#         return "happy"
#     elif any(word in lowered for word in ["alert", "warning", "watch out", "danger"]):
#         return "alert"
#     elif any(word in lowered for word in ["sarcasm", "really?", "sure", "yeah right"]):
#         return "sarcastic"
#     elif any(word in lowered for word in ["calm", "relax", "easy", "chill"]):
#         return "calm"
#     elif any(word in lowered for word in ["intense", "serious", "now", "focus"]):
#         return "intense"
#     else:
#         return "default"
