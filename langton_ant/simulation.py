# ruff: noqa: D100,S311,E501

from pathlib import Path

import pygame
import yaml

from .board import Board
from .state import State


class Simulation:
    """The main class of the simulation."""

    def __init__(self, steps: int, path: str, gui_mode: bool,  # noqa: FBT001, PLR0913
                 fps: int, tile_size: int, ant_color: str) -> None:
        """Init."""
        self._steps = steps
        self._path = path
        self._gui_mode = gui_mode
        self._fps = fps
        self._tile_size = tile_size
        self._ant_color = ant_color

    def _init(self) -> None:
        """Initialize the simulation."""
        # Create the board
        self._board = Board(self._tile_size, self._ant_color)

        # Initialize pygame for GUI mode
        if self._gui_mode:
            pygame.init()
            self._screen = pygame.display.set_mode((20*self._tile_size, 20*self._tile_size))
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
        self._state = State.SIMULATING

        # Simulation loop
        while self._state == State.SIMULATING:
            # Simulate a step
            self._board.simulate()

            # Wait 1/FPS second
            self._clock.tick(self._fps)

            for event in pygame.event.get():
                # Closing window
                if event.type == pygame.QUIT:
                    self._state = State.QUIT

                # Key press
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_q:
                            self._state = State.QUIT

            self._board.draw(self._screen)

            # Display the current step number
            pygame.display.set_caption(f"Step : {c}")

            # Display
            pygame.display.update()

            c += 1

        pygame.quit()
