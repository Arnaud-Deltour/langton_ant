# ruff: noqa: D100,S311,E501

from pathlib import Path

import yaml

from .board import Board


class Simulation:
    """The main class of the simulation."""

    def __init__(self, steps: int, path: str) -> None:
        """Init."""
        self._steps = steps
        self._path = path

    def _init(self) -> None:
        """Initialize the simulation."""
        # Create the board
        self._board = Board()

    def start(self) -> None:
        """Start the simulation."""
        # Initialize simulation
        self._init()
        c = self._steps

        # Simulation loop
        while c != 0:
            # Simulate a step
            self._board.simulate()

            # Decrease the number of steps left
            c -= 1

        # Write the result either in command line or in the given file
        if self._path is None:
            print(f"Step {self._steps}")  # noqa: T201
            print(self._board.str_output())  # noqa: T201
        else:
            with Path(self._path).open("w") as f:
                yaml.safe_dump(self._board.yml_output(self._steps), f, default_style=None, sort_keys=False)
