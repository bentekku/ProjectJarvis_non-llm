from voice.voice_io import listen, speak

# Acceptable affirmative responses
affirmatives = {
    "yes",
    "sure",
    "go ahead",
    "please do",
    "definitely",
    "absolutely",
    "be my guest",
    "okay",
    "yep",
}
negatives = {"no", "stop", "that's enough", "nah", "not now", "cancel", "nope"}


def should_continue() -> bool:
    """
    Ask user for permission to keep reading.
    """
    speak("Shall I keep reading the summary, Sir?")
    reply = listen().strip().lower()
    return any(word in reply for word in affirmatives)


def read_in_chunks(summary: str, chunk_size: int = 75) -> str:
    """
    Speaks the summary in chunks and checks after each chunk if user wants to continue.
    """
    words = summary.split()
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i : i + chunk_size])
        speak(chunk)

        # Ask only if there's more to read
        if i + chunk_size < len(words):
            if not should_continue():
                speak("Alright, stopping here, sir.")
                # return "Stopped reading as instructed, boss."
        return "That's all from the summary, boss."
