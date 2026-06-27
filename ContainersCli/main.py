from cli import parse_arguments
from validation import validate
from docker_runner import run_container


def main():
    args = parse_arguments()

    validate(args)

    run_container(
        image=args.image,
        path=args.path,
        shell="bash"
    )


if __name__ == "__main__":
    main()