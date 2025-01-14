# ruff: noqa: D100,S311,E501

import enum


class Color(enum.Enum):
    """Color of tile."""

    WHITE = " "
    BLACK = "X"
