def get_gamma_and_epsilon(values):
    def most_common(values, position):
        num_values = len(values)
        num_ones = sum(int(v[position]) for v in values)
        return "1" if num_ones >= (num_values / 2) else "0"

    num_bits = len(values[0])
    gamma = int("".join(most_common(values, p) for p in range(num_bits)), 2)
    mask = int("1" * num_bits, 2)
    epsilon = gamma ^ mask

    return gamma, epsilon


def get_rating(values, to_match):
    num_bits = len(values[0])

    for p in range(num_bits):
        mask = 1 << (num_bits - p - 1)
        comp = to_match(values)
        values = [v for v in values if (int(v, 2) & mask) ^ (comp & mask) == 0]

        if len(values) == 1:
            break

    assert len(values) == 1
    return int(values[0], 2)


if __name__ == "__main__":
    with open("input", "r") as f:
        values = f.read().splitlines()

    gamma, epsilon = get_gamma_and_epsilon(values)
    print(gamma * epsilon)

    oxygen = get_rating(values, lambda v: get_gamma_and_epsilon(v)[0])
    co2 = get_rating(values, lambda v: get_gamma_and_epsilon(v)[1])
    print(oxygen * co2)
