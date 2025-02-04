# ruff: noqa: D100,S311,E501

from pathlib import Path

import pygame
import yaml

from .board import Board


class Simulation:
    """The main class of the simulation."""

    def __init__(self, steps: int, path: str, gui_mode: bool) -> None:  # noqa: FBT001
        """Init."""
        self._steps = steps
        self._path = path
        self._gui_mode = gui_mode

    def _init(self) -> None:
        """Initialize the simulation."""
        # Create the board
        self._board = Board()

        # Initialize pygame for GUI mode
        if self._gui_mode:
            pygame.init()
            self._screen = pygame.display.set_mode((400,400))
            self._clock = pygame.time.Clock()

    def start(self) -> None:
        """Start the simulation."""
        # Initialize simulation
        self._init()

        if self._gui_mode:
            self.gui_simulation()
        else:
            self.normal_simulation()

    def normal_simulation(self) -> None:
        """Simulate for text output."""
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

    def gui_simulation(self) -> None:
        """Simulate for GUI output."""
        c = 0

        # Simulation loop
        while True:
            # Simulate a step
            self._board.simulate()

            # Wait 1/FPS second
            self._clock.tick(10)

            for event in pygame.event.get():
                # Closing window
                if event.type == pygame.QUIT:
                    pygame.quit()

                # Key press
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_q:
                            pygame.quit()

            self._board.draw(self._screen)

            # Display the current step number
            pygame.display.set_caption(f"Step : {c}")

            # Display
            pygame.display.update()

            c += 1
