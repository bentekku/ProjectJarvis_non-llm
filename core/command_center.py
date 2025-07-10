import importlib
import os
from pathlib import Path

skills = []

# Dynamically load skills from the skills/ directory recursively
skills_path = Path(__file__).parent.parent / "skills"

for root, _, files in os.walk(skills_path):
    for file in files:
        if file.endswith(".py") and not file.startswith("__"):
            full_path = Path(root) / file
            relative_path = full_path.relative_to(skills_path.parent).with_suffix("")
            module_name = ".".join(relative_path.parts)

            try:
                mod = importlib.import_module(module_name)
                if hasattr(mod, "can_handle") and hasattr(mod, "handle"):
                    skills.append(mod)
            except Exception as e:
                print(f"[Jarvis Loader Error]: Failed to load {module_name}: {e}")


def handle_command(command: str) -> str:
    command = command.lower().strip()
    for skill in skills:
        if skill.can_handle(command):
            return skill.handle(command)
    return "Sorry boss, currently I'm operating at the fraction of my full capacity."

    #     # ⏱ Timer
    #     if "timer" in command:
    #         return handle_timer(command)

    # # 🧭 App & Folder
    # if command.startswith("open"):
    #     return handle_open(command)

    # # 🎶 Custom link
    # if any(phrase in command for phrase in ["play some funk", "fire up funk music"]):
    #     return open_link("phonk-playlist")

    # # 🌐 Wiki Search
    # if command.startswith(("who is", "what is", "define")):
    #     return handle_wiki(command)

    # # 🔍 Google Search
    # if "search google for" in command:
    #     topic = command.replace("search google for", "").strip()
    #     return google_search(topic)

    # # 🔎 Web Scrape
    # if "loop up" in command:
    #     topic = command.replace("look up", "").strip()
    #     return web_scrape_snippet(topic)


# # -------------------------------------------
# # 💥 Subcommand Handlers
# # -------------------------------------------


# def handle_timer(command: str) -> str:
#     try:
#         seconds = parse_duration(command)
#         if seconds > 0:
#             set_timer(seconds)
#             return "Timer set boss. You'll will be notified."
#         return "I couldn't understand how long to set the timer for."
#     except Exception as e:
#         return f"Something went wrong while setting the timer: {str(e)}"


# def handle_open(command: str) -> str:
#     words = command.split("open", 1)[-1].strip()
#     if any(folder in words for folder in get_known_folders):
#         return open_folder(words)
#     return open_app(words)


def handle_wiki(command: str) -> str:
    for prefix in ["who is", "what is", "define"]:
        if command.startswith(prefix):
            topic = command.replace(prefix)
            return search_wikipedia(topic)
        return "Sorry boss, I couldn't figure out what to look up on Wikipedia."
