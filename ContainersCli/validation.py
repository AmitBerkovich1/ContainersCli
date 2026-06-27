from pathlib import Path
import shutil
import sys


def validate(args):
    validate_docker_installed()
    validate_directory(args.path)


def validate_directory(path):
    project = Path(path)

    if not project.exists():
        print(f"Directory '{path}' does not exist.")
        sys.exit(1)

    if not project.is_dir():
        print(f"'{path}' is not a directory.")
        sys.exit(1)


def validate_docker_installed():
    if shutil.which("docker") is None:
        print("Docker is not installed or not in PATH.")
        sys.exit(1)
