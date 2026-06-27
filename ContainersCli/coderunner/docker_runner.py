from subprocess import run
from logging import Logger
from subprocess import DEVNULL
from coderunner.utils import absolute_path

WORKSPACE = "/workspace"


def run_container(image: str, path: str, shell: str, command: list[str] | None, name: str,
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

    if command:
        logger.info("Running Commands")
        docker_command += command
    else:
        logger.info("Opening Interactive shell")
        docker_command.append(shell)

    logger.info("Running Docker container...")
    logger.info(" ".join(docker_command))

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
