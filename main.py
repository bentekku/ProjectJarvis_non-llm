from voice.voice_io import listen, speak
from core.command_center import handle_command

def main():
    
    speak("Jarvis online. How can I assist you, boss?")
    while True:
        command = listen()
        if not command:
            continue
        if command in ["exit", "quit", "stop"]:
            speak("Goodbye, boss!")
            break
        response = handle_command(command)
        speak(response)

if __name__ == "__main__":
    main()
