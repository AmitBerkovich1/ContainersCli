from subprocess import run
from logging import Logger
from subprocess import DEVNULL
from coderunner.utils import absolute_path
from coderunner.utils import handle_commands

WORKSPACE = "/workspace"


def run_container(image: str, path: str, shell: str, commands: list[list[str]] | None, name: str,
                  logger: Logger):
    local_path = absolute_path(path)

    pull_image(image, logger)

    docker_command = [
        "docker",
        "run",
        "--name",
        name,
        "--rm",
        "-it",
        "-v",
        f"{local_path}:{WORKSPACE}",
        "-w",
        WORKSPACE,
        image
    ]

    if commands:
        logger.info("Running Commands")
        commands_as_string = handle_commands(commands)
        docker_command += ["bash", "-c", commands_as_string]
    else:
        logger.info("Opening Interactive shell")
        docker_command.append(shell)

    logger.info("Running Docker container...")
    logger.info(f"running docker command: {docker_command}")

    run(docker_command)


def image_exists(image: str):
    result = run(
        ["docker", "image", "inspect", image],
        stdout=DEVNULL,
        stderr=DEVNULL
    )

    return result.returncode == 0


def pull_image(image: str, logger: Logger):
    if image_exists(image):
        logger.info("Image already exists locally.")
        return

    logger.info(f"Pulling {image} ...")
    run(["docker", "pull", image], check=True)
