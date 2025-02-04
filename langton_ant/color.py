# ruff: noqa: D100,S311,E501

import enum


class Color(enum.Enum):
    """Color of tile."""

    WHITE = "#FFFFFF"
    BLACK = "#000000"
    RED = "#FF0000"

    def __str__(self) -> str:
        """Return a string value."""
        if self == Color.WHITE:
            return " "
        return "X"
