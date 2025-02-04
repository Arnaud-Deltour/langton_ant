# ruff: noqa: D100,S311,E501

# First party
import pygame

from .color import Color
from .dir import Dir


class Ant:
    """Ant object."""

    def __init__(self, x: int, y: int, direction: Dir) -> None:
        """Init."""
        self._x = x
        self._y = y
        self._direction = direction

    def gui_init(self, tile_size: int, color: str) -> None:
        """GUI mode init."""
        self._tile_size = tile_size
        self._color = color

        # Load ant image on all rotations
        self._image_up = pygame.transform.scale(pygame.image.load("ant.png").convert_alpha(),
                                                (self._tile_size*0.7,self._tile_size*0.9))
        self._image_left = pygame.transform.rotate(self._image_up, 90)
        self._image_down = pygame.transform.rotate(self._image_up, 180)
        self._image_right = pygame.transform.rotate(self._image_up, 270)

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

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the ant."""
        match self._direction:
            case Dir.UP:
                self._image_up.fill(self._color, special_flags=pygame.BLEND_RGB_MAX)
                screen.blit(self._image_up, (self._x*self._tile_size + 10.15*self._tile_size,
                                             -self._y*self._tile_size + 10.05*self._tile_size))
            case Dir.LEFT:
                self._image_left.fill(self._color, special_flags=pygame.BLEND_RGB_MAX)
                screen.blit(self._image_left, (self._x*self._tile_size + 10.05*self._tile_size,
                                             -self._y*self._tile_size + 10.15*self._tile_size))
            case Dir.DOWN:
                self._image_down.fill(self._color, special_flags=pygame.BLEND_RGB_MAX)
                screen.blit(self._image_down, (self._x*self._tile_size + 10.15*self._tile_size,
                                             -self._y*self._tile_size + 10.05*self._tile_size))
            case Dir.RIGHT:
                self._image_right.fill(self._color, special_flags=pygame.BLEND_RGB_MAX)
                screen.blit(self._image_right, (self._x*self._tile_size + 10.05*self._tile_size,
                                             -self._y*self._tile_size + 10.15*self._tile_size))
