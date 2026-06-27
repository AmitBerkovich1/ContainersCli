from pathlib import Path


def absolute_path(path: str) -> str:
    return str(Path(path).resolve())


def handle_commands(command_list: list[list[str]]) -> str:
    commands_as_string = ""
    for commands in command_list:
        commands_as_string += commands[0] + " && "
    return commands_as_string[:-3]
