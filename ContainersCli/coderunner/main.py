from logging import INFO
from coderunner.cli import parse_arguments
from coderunner.validation import validate
from coderunner.docker_runner import run_container
from coderunner.logger import setup_logger


def main():
    args = parse_arguments()

    logger = setup_logger(
        level=INFO
    )

    logger.info("Starting running process...")

    validate(args, logger)

    run_container(
        image=args.image,
        path=args.path,
        shell=args.shell,
        name=args.name,
        commands=args.command,
        logger=logger
    )


if __name__ == "__main__":
    main()
