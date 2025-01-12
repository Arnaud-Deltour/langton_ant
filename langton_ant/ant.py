from .dir import Dir
from .color import Color

class Ant:
    """Ant object."""

    def __init__(self, x: int, y: int, direction: Dir):
        self._x = x
        self._y = y
        self._direction = direction

    def turn(self, color) -> None:
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

    def move(self):
        """Move the ant."""
        self._x += self._direction.x
        self._y += self._direction.y

    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y
    
    @property
    def direction(self) -> Dir:
        return self._direction
    