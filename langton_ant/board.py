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

    def gui_init(self, tile_size: int, ant_color: str) -> None:
        """GUI mode init."""
        self._tile_size = tile_size
        self._ant.gui_init(tile_size, ant_color)

    def grid(self) -> list[list[str]]:
        """Represent the board state in a matrix."""
        # Create a blank grid with the right size
        self._x_min, self._x_max, self._y_min, self._y_max = self.get_range()
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

    def get_range(self) -> tuple[int,int,int,int]:
        """Get min and max x and y values explored."""
        keys = self._tiles.keys()
        return min([k[0] for k in keys]), max([k[0] for k in keys]), min([k[1] for k in keys]), max([k[1] for k in keys])

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the board state."""
        # Create a surface with the right size to show everything
        self._x_min, self._x_max, self._y_min, self._y_max = self.get_range()
        size = max((self._x_max-self._x_min + 3)*self._tile_size,(self._y_max-self._y_min + 3)*self._tile_size)
        surf = pygame.Surface((size,size))

        # White background
        surf.fill((255,255,255))

        # Black tiles drawing
        for c in self._tiles:
            if self._tiles[c] == Color.BLACK:
                rect = pygame.Rect((c[0]-self._x_min + 1) * self._tile_size,
                                   (-c[1]+self._y_max + 1) * self._tile_size,
                                   self._tile_size, self._tile_size)
                pygame.draw.rect(surf, Color.BLACK.value, rect)

        # Draw the ant
        self._ant.draw(surf, self._x_min, self._y_max)

        # Scale the surface to the screen and blit it
        surface = pygame.transform.scale(surf, (self._tile_size*20,self._tile_size*20))
        screen.blit(surface, (0,0))
