# ruff: noqa: D100,S311,E501

import enum


class State(enum.Enum):
    """State class."""

    QUIT = 0
    SIMULATING = 1
