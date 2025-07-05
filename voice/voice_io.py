import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize TTS engine once for efficiency
engine = pyttsx3.init()

def speak(text):
  """Speaks out loud using pyttsx3"""
  engine.say(text)
  engine.runAndWait()

def listen():
  """Listens to microphone and returns recognized text"""
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Jarvis: Listening...")
    audio = recognizer.listen(source)
  try:
    command = recognizer.recognize_google(audio)
    print(f"You said: {command}")
    return command.lower()
  except sr.UnknownValueError:
    print("Sorry, I didn't catch that.")
  except sr.RequestError:
    print("Sorry, there was an error with the speech recognition service.")
    return ""
  
  def get_time():
    """Returns the current time as a string"""
    now = datetime.now()
    return now.strftime("The time is %I:%M %p")
  
  def get_date():
    """Returns the current date as a string"""
    now = datetime.now()
    return now.strftime("Today is %B %d, %Y")
  
  def get_day_name():
    """Returns the current day of the week name as a string"""
    now = datetime.now()
    return now.strftime("It's %A today")
  
  def get_day_number():
    now = datetime.now()
    return f"Today is day number {now.isoweekday()} of the week"
  
  def main():
    speak("Jarvis is online. How can I help you, boss?")
    while True:
      command = listen()
      if not command:
        continue
      if "time" in command:
        speak(get_time)
      elif "date" in command:
        speak(get_date())
      elif "day" in command:
        speak(get_day_name())
      elif "day number" in command:
        speak(get_day_number())
      elif "exit" in command or "quit" in command:
        speak("Goodbye, boss!")
        break
      else:
        speak("Sorry boss, for now I have limited capabilities. I can only assist you with time, date, and day right now.")

    if __name__ == "__main__":
      main()