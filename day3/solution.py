import copy
import numpy as np


def read_line(line):
    return np.array([int(d) for d in line.strip()])


def read_input(path):
    with open(path) as f:
        input = [read_line(line) for line in f]
    return input


def array_to_decimal(array):
    return int(''.join([str(int(d)) for d in array]), 2)


def get_binary_rates(numbers):
    n = len(numbers)
    pos = sum(numbers)
    neg = n - pos
    gamma_array = [1 if p >= n else 0 for p, n in zip(pos, neg)]
    delta_array = [1 - i for i in gamma_array]
    return gamma_array, delta_array


def get_rates(numbers):
    gamma_array, delta_array = get_binary_rates(numbers)
    gamma = array_to_decimal(gamma_array)
    delta = array_to_decimal(delta_array)
    return gamma, delta


def filter_on_position(numbers, position, inverse_filter):
    gamma, delta = get_binary_rates(numbers)
    if not inverse_filter:
        ref = gamma[position]
    else:
        ref = delta[position]

    to_delete = []
    for i_num, num in enumerate(numbers):
        if num[position] != ref:
            to_delete.append(i_num)
    numbers = [n for i_n, n in enumerate(numbers) if i_n not in to_delete]
    return numbers


def get_oxygen_rate(numbers):
    n = copy.deepcopy(numbers)
    for k in range(len(numbers[0])):
        n = filter_on_position(n, k, False)
        if len(n) == 1:
            return array_to_decimal(n[0])


def get_co2_rate(numbers):
    n = copy.deepcopy(numbers)
    for k in range(len(numbers[0])):
        n = filter_on_position(n, k, True)
        if len(n) == 1:
            return array_to_decimal(n[0])


if __name__ == "__main__":
    numbers = read_input("input.txt")
    gamma_rate, delta_rate = get_rates(numbers)
    print(
        f'gamma: {gamma_rate}, delta: {delta_rate},'
        f'product: {gamma_rate * delta_rate}'
    )
    oxygen = get_oxygen_rate(numbers)
    co2 = get_co2_rate(numbers)
    print(
        f'oxygen: {oxygen}, co2: {co2},'
        f'product: {oxygen * co2}'
    )
