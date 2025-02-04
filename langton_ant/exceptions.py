# ruff: noqa: D100,S311,E501

class ColorError(Exception):
    """Exception for color format error."""

    def __init__(self, color: str) -> None:
        """Object initialization."""
        super().__init__(f'Color "{color}" does not respect the HTML'
                         ' hexadecimal format #rrggbb.')
