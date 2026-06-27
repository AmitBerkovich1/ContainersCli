from pathlib import Path


def absolute_path(path: str) -> str:
    return str(Path(path).resolve())
