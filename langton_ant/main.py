# ruff: noqa: D100,S311,E501

import logging

import colorlog

from .cmd_line import read_args
from .simulation import Simulation


def main() -> None:
    """Read arguments and start the simulation."""
    # Verbose init
    logger = logging.getLogger("foo")
    color_fmt = colorlog.ColoredFormatter(
    "%(log_color)s[%(asctime)s][%(levelname)s] %(message)s",
    log_colors={
        "DEBUG": "yellow",
        "INFO": "green",
        "WARNING": "purple",
        "ERROR": "red",
        "CRITICAL": "red",
        })
    color_handler = colorlog.StreamHandler()
    color_handler.setFormatter(color_fmt)
    logger.addHandler(color_handler)

    # Read command line arguments
    args = read_args()

    # Set verbose level
    if args.verbose == 1:
        logger.setLevel(logging.INFO)
    elif args.verbose == 2:  # noqa: PLR2004
        logger.setLevel(logging.DEBUG)

    # Start automata
    Simulation(steps = args.steps, path = args.path, gui_mode=args.gui,
               fps=args.fps, tile_size=args.tile_size, ant_color=args.ant_color,
               logger = logger).start()
