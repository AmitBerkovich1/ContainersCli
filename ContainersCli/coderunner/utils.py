from pathlib import Path
from shlex import join


def absolute_path(path: str) -> str:
    return str(Path(path).resolve())


def handle_commands(command_list: list[list[str]]) -> str:
    return " && ".join(join(cmd) for cmd in command_list)
