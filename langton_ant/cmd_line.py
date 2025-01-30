# ruff: noqa: D100,S311,E501

import argparse

DEFAULT_STEPS = 10

def read_args() -> argparse.Namespace:
    """Read command line arguments."""
    # Parser and its description
    parser = argparse.ArgumentParser(description="The Langton's ant.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Simulation options
    parser.add_argument("--steps", "-s", type=int,
                        default=DEFAULT_STEPS,
                        help="Number of steps to compute.")

    parser.add_argument("--path", "-p", type=str, default=None, help="Output file path.")

    # Parse
    args = parser.parse_args()

    return args  # noqa: RET504
