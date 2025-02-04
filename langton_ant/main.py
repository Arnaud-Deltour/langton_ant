# ruff: noqa: D100,S311,E501

from .cmd_line import read_args
from .simulation import Simulation


def main() -> None:
    """Read arguments and start the simulation."""
    # Read command line arguments
    args = read_args()

    # Start automata
    Simulation(steps = args.steps, path = args.path, gui_mode=args.gui).start()
