import speech_recognition as sr
import pyttsx3

# Initialize TTS engine once
engine = pyttsx3.init()

# Try to set the voice to 'George' from UK voice pack
def set_jarvis_voice():
    voices = engine.getProperty('voices')

    for voice in voices:
        # Debug voice names and IDs to see what's available
        # print(f"Name: {voice.name}, ID: {voice.id}")
        if "george" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            print(f"✅ Using voice: {voice.name}")
            return
        if "en-gb" in voice.id.lower() or "english (united kingdom)" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            print(f"✅ Using fallback UK voice: {voice.name}")
            return

    print("⚠️ UK voice not found. Using default voice.")

set_jarvis_voice()
engine.setProperty('rate', 160)

def speak(text: str) -> None:
    """
    Convert text to speech and speak it out loud.
    """
    engine.say(text)
    engine.runAndWait()

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
        speak("Speech service is unavailable.")
        return ""
