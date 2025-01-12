from .cmd_line import read_args
from .simulation import Simulation


def main():
    
    # Read command line arguments
    args = read_args()

    # Start automata
    Simulation(steps = args.steps).start()