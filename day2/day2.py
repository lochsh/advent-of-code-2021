import functools
import operator

import numpy as np


def calculate_position(course):
    units = {
        "forward": np.array([1, 0]),
        "up": np.array([0, -1]),
        "down": np.array([0, 1]),
    }

    def get_position_change(string):
        direction, quantity = string.split()
        return units[direction] * int(quantity)

    return functools.reduce(
        operator.add,
        map(get_position_change, course),
    )


def calculate_position_with_aim(course):
    aim = 0
    depth = 0
    horiz = 0
    for c in course:
        direction, quantity = c.split()
        quantity = int(quantity)

        if direction == "up":
            aim -= quantity
        elif direction == "down":
            aim += quantity
        elif direction == "forward":
            horiz += quantity
            depth += aim * quantity

    return horiz, depth


if __name__ == "__main__":
    with open("input", "r") as f:
        course = f.readlines()

    horiz, depth = calculate_position(course)
    print(horiz * depth)
    new_horiz, new_depth = calculate_position_with_aim(course)
    print(new_horiz * new_depth)
