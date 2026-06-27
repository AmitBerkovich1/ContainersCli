from pathlib import Path
from shutil import which
from sys import exit
from logging import Logger


def validate(args, logger: Logger):
    validate_docker_installed(logger)
    validate_directory(args.path, logger)


def validate_directory(path, logger: Logger):
    project = Path(path)

    if not project.exists():
        logger.error(f"Directory '{path}' does not exist.")
        exit(1)

    if not project.is_dir():
        logger.error(f"'{path}' is not a directory.")
        exit(1)


def validate_docker_installed(logger: Logger):
    if which("docker") is None:
        logger.error("Docker is not installed or not in PATH.")
        exit(1)
