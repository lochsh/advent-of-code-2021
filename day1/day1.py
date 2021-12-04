import collections
import functools
import itertools


def increment_if_increased(value, pair):
    prev, current = pair
    if prev < current:
        return value + 1
    return value


def count_increased():
    with open("input", "r") as f:
        readings = map(int, f.readlines())

    return functools.reduce(
        increment_if_increased,
        itertools.pairwise(readings),
        0,
    )


def count_increased_sliding_window():
    with open("input", "r") as f:
        readings = list(map(int, f.readlines()))

    def sliding_sum():
        width = 3
        window = collections.deque(readings[:width], maxlen=width)
        yield sum(window)

        for r in readings[width:]:
            window.append(r)
            yield sum(window)

    return functools.reduce(
        increment_if_increased,
        itertools.pairwise(sliding_sum()),
        0,
    )


if __name__ == "__main__":
    print(count_increased())
    print(count_increased_sliding_window())
