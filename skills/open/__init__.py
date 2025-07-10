from skills.open.open_apps import handle as handle_app, can_handle as can_handle_app
from skills.open.open_folder import (
    handle as handle_folder,
    can_handle as can_handle_folder,
)
from skills.open.open_link import handle as handle_link, can_handle as can_handle_link


def can_handle(command: str) -> bool:
    command = command.lower()
    return any(
        checker(command)
        for checker in [can_handle_app, can_handle_folder, can_handle_link]
    )


def handle(command: str) -> str:
    command = command.lower()

    if can_handle_link(command):
        return handle_link(command)
    elif can_handle_folder(command):
        return handle_folder(command)
    elif can_handle_app(command):
        return handle_app(command)

    return "Sorry boss, I couldn't figure out what to open."
