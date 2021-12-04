def get_gamma_and_epsilon():
    def most_common(values, position):
        num_values = len(values)
        num_ones = sum(int(v[position]) for v in values)
        return "1" if num_ones > (num_values / 2) else "0"

    with open("input", "r") as f:
        values = f.read().splitlines()

    num_bits = len(values[0])
    gamma = int("".join(most_common(values, p) for p in range(num_bits)), 2)
    mask = int("1" * num_bits, 2)
    epsilon = gamma ^ mask

    return gamma, epsilon


if __name__ == "__main__":
    gamma, epsilon = get_gamma_and_epsilon()
    print(gamma * epsilon)
