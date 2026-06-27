from pathlib import Path
import platform


def absolute_path(path: str) -> str:
    return str(Path(path).resolve())


def is_windows() -> bool:
    return platform.system().lower() == "windows"
