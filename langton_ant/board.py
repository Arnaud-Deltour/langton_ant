# ruff: noqa: D100,S311,E501

from typing import Any

import pygame

from .ant import Ant
from .color import Color
from .dir import Dir


class Board:
    """Class that stores the state of the simulation."""

    def __init__(self) -> None:
        """Init."""
        self._tiles = {(0,0):Color.WHITE}
        self._ant = Ant(0, 0, Dir.UP)

    def grid(self) -> list[list[str]]:
        """Represent the board state in a matrix."""
        # Create a blank grid with the right size
        keys = self._tiles.keys()
        self._x_min = min([k[0] for k in keys])
        self._x_max = max([k[0] for k in keys])
        self._y_min = min([k[1] for k in keys])
        self._y_max = max([k[1] for k in keys])
        grid = [[" " for j in range(self._x_max-self._x_min+1)] for i in range(self._y_max-self._y_min+1)]

        # Fill the grid with the tiles known
        for c in self._tiles:
            grid[-c[1]+self._y_max][c[0]-self._x_min] = str(self._tiles[c])

        return grid

    def str_output(self) -> str:
        """Give the state as a text."""
        grid = self.grid()

        return f"{self._y_max - self._ant.y},{self._ant.x - self._x_min},{self._ant.direction.name}\n{''.join(''.join(grid[k]) + "\n" for k in range(len(grid)))}"

    def yml_output(self, step:int) -> dict[str, Any]:
        """Give the state as a dict."""
        grid = self.grid()

        return {"step": step, "ant": f"{self._y_max - self._ant.y},{self._ant.x - self._x_min},{self._ant.direction.name}",
                  "grid": ["".join(grid[i][k] for k in range(len(grid[i]))) for i in range(len(grid))]}

    def simulate(self) -> None:
        """Simulate a step."""
        current_tile = (self._ant.x, self._ant.y)

        # Turn the ant
        self._ant.turn(self._tiles[current_tile])

        # Change tile color
        if self._tiles[current_tile] == Color.WHITE:
            self._tiles[current_tile] = Color.BLACK
        else:
            self._tiles[current_tile] = Color.WHITE

        # Move the ant
        self._ant.move()
        if (self._ant.x, self._ant.y) not in self._tiles:
            self._tiles[(self._ant.x, self._ant.y)] = Color.WHITE

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the board state."""
        # White background
        screen.fill((255,255,255))

        # Black tiles drawing
        for c in self._tiles:
            if self._tiles[c] == Color.BLACK:
                rect = pygame.Rect(c[0] * 20+200, -c[1] * 20+200, 20, 20)
                pygame.draw.rect(screen, Color.BLACK.value, rect)

        # Drawing the ant
        self._ant.draw(screen)
