# ruff: noqa: D100,S311,E501

# First party
import pygame

from .color import Color
from .dir import Dir


class Ant:
    """Ant object."""

    def __init__(self, x: int, y: int, direction: Dir, color: str) -> None:
        """Init."""
        self._x = x
        self._y = y
        self._direction = direction
        self._color = color

    def turn(self, color: Color) -> None:
        """Turn the ant depending on the color."""
        if color == Color.WHITE:
            match self._direction:
                case Dir.UP:
                    self._direction = Dir.RIGHT
                case Dir.RIGHT:
                    self._direction = Dir.DOWN
                case Dir.DOWN:
                    self._direction = Dir.LEFT
                case Dir.LEFT:
                    self._direction = Dir.UP

        else:
            match self._direction:
                case Dir.UP:
                    self._direction = Dir.LEFT
                case Dir.LEFT:
                    self._direction = Dir.DOWN
                case Dir.DOWN:
                    self._direction = Dir.RIGHT
                case Dir.RIGHT:
                    self._direction = Dir.UP

    def move(self) -> None:
        """Move the ant."""
        self._x += self._direction.x
        self._y += self._direction.y

    @property
    def x(self) -> int:
        """X position."""
        return self._x

    @property
    def y(self) -> int:
        """Y position."""
        return self._y

    @property
    def direction(self) -> Dir:
        """Ant direction."""
        return self._direction

    def draw(self, screen: pygame.Surface, tile_size: int) -> None:
        """Draw the ant."""
        if self._direction in (Dir.RIGHT, Dir.LEFT):
            rect = pygame.Rect(self._x * tile_size + 10*tile_size + tile_size*0.1,
                               -self._y * tile_size + 10*tile_size + tile_size*0.4, tile_size*0.8, tile_size*0.2)
        else:
            rect = pygame.Rect(self._x * tile_size + 10*tile_size + tile_size*0.4,
                               -self._y * tile_size + 10*tile_size + tile_size*0.1, tile_size*0.2, tile_size*0.8)

        pygame.draw.rect(screen, self._color, rect)
