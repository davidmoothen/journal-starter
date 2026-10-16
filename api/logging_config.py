"""Application logging configuration, completed in Task 3."""

import logging


def configure_logging(level: int = logging.INFO) -> None:
    """Configure logging for the application."""
    logging.basicConfig(level=level)
    if not logging.root.handlers:
        logging.root.addHandler(logging.StreamHandler())
    logging.root.setLevel(level)
    # logging.basicConfig(
    #     level=level, handlers=logging.root.handlers if logging.root.handlers is not None else [logging.StreamHandler()])

    # logging.root.setLevel(level)
