import functools
import operator

import numpy as np


def calculate_position():
    units = {
        "forward": np.array([1.0, 0.0]),
        "up": np.array([0.0, -1.0]),
        "down": np.array([0.0, 1.0]),
    }

    def get_position_change(string):
        direction, quantity = string.split()
        return units[direction] * float(quantity)

    with open("input", "r") as f:
        return functools.reduce(
            operator.add,
            map(get_position_change, f.readlines()),
        )


if __name__ == "__main__":
    horiz, vert = calculate_position()
    print(horiz * vert)
