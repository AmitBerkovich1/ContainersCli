import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
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

    return parser.parse_args()
