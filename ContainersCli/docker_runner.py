from subprocess import run
from subprocess import DEVNULL
from subprocess import DEVNULL
from utils import absolute_path

WORKSPACE = "/workspace"


def run_container(image: str, path: str, shell: str, command: list[str] | None, name: str):
    local_path = absolute_path(path)

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
        docker_command += command
    else:
        docker_command.append(shell)

    print("\nRunning Docker container...\n")
    print(" ".join(docker_command))
    print()

    run(docker_command)


def image_exists(image: str):
    result = run(
        ["docker", "image", "inspect", image],
        stdout=DEVNULL,
        stderr=DEVNULL
    )

    return result.returncode == 0


def pull_image(image: str):
    if image_exists(image):
        print("Image already exists locally.")
        return

    print(f"Pulling {image} ...")
    run(["docker", "pull", image], check=True)
