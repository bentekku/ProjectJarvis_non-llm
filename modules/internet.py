import wikipediaapi
import webbrowser
import requests
from bs4 import BeautifulSoup
from voice.voice_io import speak
from utils.read_chunks import read_in_chunks

# Proper user-agent and language
wiki = wikipediaapi.Wikipedia(
    language="en", user_agent="JarvisBot/1.0 (https://github.com/IamSh/ProjectJarvis)"
)


def search_wikipedia(query: str) -> str:
    """
    Searches Wikipedia using wikipedia-api and returns a summary.
    """
    try:
        page = wiki.page(query)

        if page.exists():
            summary = page.summary.strip()
            if summary:
                return read_in_chunks(summary)
            else:
                return "The page exists, but it doesn't have summary, boss."
        else:
            return f"I couldn't find {query} on Wikipedia, boss."
    except Exception as e:
        print(f"Error: {e}")
        return f"Something went wrong with the Wikipedia search."


def google_search(query: str) -> str:
    """
    Opens a Google search in browser.
    """
    speak("On it boss. Searching the Google.")
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"I've searched Google for: {query}"


def web_scrape_snippet(query: str) -> str:
    """
    Try to get a quick answer from the web (like Google's featured snippet).
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        url = f"https://www.google.com/search?q={query}"
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        answer_box = soup.find("div", class_="BNeawe").text
        return f"Here's what I've found: {answer_box}"
    except Exception:
        return "Couldn't find a direct answer online, boss."
