from argparse import ArgumentParser
from argparse import REMAINDER
from uuid import uuid4


def parse_arguments():
    parser = ArgumentParser(
        description="Run Your Local Code Easily On a Container"
    )

    parser.add_argument(
        "--image",
        required=True,
        help="Docker image to use"
    )

    parser.add_argument(
        "--path",
        required=True,
        help="Path to local project directory to run"
    )

    parser.add_argument(
        "--shell",
        default="bash",
        help="Shell to open inside the container"
    )

    parser.add_argument(
        "--name",
        default=str(uuid4()),
        help="Name of the created container"
    )

    parser.add_argument(
        "--command",
        required=False,
        nargs=REMAINDER,
        help="Command to run inside the container"
    )

    return parser.parse_args()
