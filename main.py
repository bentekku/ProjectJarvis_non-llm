import atexit
from voice.voice_io import listen, speak
from core.command_center import handle_command
from core.voice_manager import cleanup_temp_folder


def main():

    speak("Jarvis system boot complete, boss. Awaiting commands.", mood="happy")
    while True:
        command = listen()
        if not command:
            continue
        if command in ["exit", "quit", "stop", "terminate"]:
            speak("Goodbye, Mr. Khan!", mood="calm")
            break
        response = handle_command(command)
        speak(response)


if __name__ == "__main__":
    main()

    # Register cleanup for temp files
atexit.register(cleanup_temp_folder)
