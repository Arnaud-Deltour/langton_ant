from .board import Board

class Simulation:
    """The main class of the simulation."""

    def __init__(self, steps: int):
        self._steps = steps

    def _init(self) -> None:
        """Initialize the simulation."""
        # Create the board
        self._board = Board()

    def start(self) -> None:
        """Starts the simulation."""

        # Initialize simulation
        self._init()
        print(f"Step {self._steps}")

        # Simulation loop
        while self._steps != 0:
            # Simulate a step
            self._board.simulate()

            # Decrease the number of steps left
            self._steps -= 1

        # Write the result
        print(self._board.state())