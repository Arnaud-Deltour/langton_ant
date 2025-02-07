# ruff: noqa: D100,S311,E501

import argparse
import re

from .color import Color
from .exceptions import ColorError

DEFAULT_STEPS = 10

def read_args() -> argparse.Namespace:
    """Read command line arguments."""
    # Parser and its description
    parser = argparse.ArgumentParser(description="The Langton's ant.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Simulation options
    parser.add_argument("--steps", "-s", type=int,
                        default=DEFAULT_STEPS,
                        help="Number of steps to compute.")

    # Path to output file
    parser.add_argument("--path", "-p", type=str, default=None, help="Output file path.")

    # GUI mode
    parser.add_argument("--gui", "-g", action="store_true", help="Enable GUI mode.")
    parser.add_argument("--fps", "-f", type=int, default=5, help="Number of frames per second.")
    parser.add_argument("--tile-size", "-t", type=int, default=35, help="Size of the tiles.")
    parser.add_argument("--ant_color", "-c", type=str, default=Color.RED.value, help="Color of the ant.")

    # Verbose option
    parser.add_argument("--verbose", "-v", dest="verbose", action="count", default=0, help="Verbose level. -v for information, -vv for debug.")

    # Parse
    args = parser.parse_args()

    # Check color
    if not re.match(r"^#[0-9a-fA-F]{6}$", args.ant_color):
        raise ColorError(args.ant_color)

    return args
