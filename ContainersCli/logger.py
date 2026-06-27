from logging import INFO
from logging import getLogger
from logging import StreamHandler
from logging import Formatter
from sys import stdout


def setup_logger(level=INFO):
    logger = getLogger("coderunner")

    if logger.handlers:  # avoid duplicate logs
        return logger

    logger.setLevel(level)

    handler = StreamHandler(stdout)

    formatter = Formatter(
        "[%(levelname)s] %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
