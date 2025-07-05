import speech_recognition as sr
import pyttsx3

# Initialize the TTS engine once for efficiency
engine = pyttsx3.init()

# Select the most Jarvis-like voice
voices = engine.getProperty('voices')
for voice in voices:
    if 'hazel' in voice.name.lower() or 'en-gb' in voice.id.lower():
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 180)  # Speed: slower = classier

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
