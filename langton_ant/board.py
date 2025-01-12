from .color import Color
from .dir import Dir
from .ant import Ant

class Board:
    """Class that stores the state of the simulation."""

    def __init__(self):
        self._tiles = {(0,0):Color.WHITE}
        self._ant = Ant(0, 0, Dir.UP)

    def state(self):
        """Give the state as a text."""
        # Create a blank grid with the right size
        keys = self._tiles.keys()
        x_min = min([k[0] for k in keys])
        x_max = max([k[0] for k in keys])
        y_min = min([k[1] for k in keys])
        y_max = max([k[1] for k in keys])
        grid = [[" " for j in range(x_max-x_min+1)] for i in range(y_max-y_min+1)]

        # Fill the grid with the tiles known
        for c in self._tiles:
            grid[-c[1]+y_max][c[0]-x_min] = self._tiles[c].value

        # Give ant position and grid text
        return f"{self._ant.x},{self._ant.y},{self._ant.direction}\n{''.join(''.join(grid[k])+"\n" for k in range(len(grid)))}"

    def simulate(self):
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
