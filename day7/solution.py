import statistics
import math


def read_input(path):
    with open(path) as f:
        line = f.readline()
    return [int(n) for n in line.split(',')]


def median(nums):
    return round(statistics.median(nums))


def centroid(nums):
    return sum(nums) / len(nums)


def fuel_consumption_1(nums, aim):
    return sum([abs(n - aim) for n in nums])


def fuel_consumption_2(nums, aim):
    distances = [abs(n - aim) for n in nums]
    return sum([d*(d + 1)/2 for d in distances])


if __name__ == '__main__':
    path = 'input.txt'
    # path = 'test_input.txt'
    pos = read_input(path)
    aim = median(pos)
    print('optimal position:', aim,
          'fuel consumption:', fuel_consumption_1(pos, aim))

    approx_aim = centroid(pos)
    candidates = range(math.floor(approx_aim - 1/2),
                       math.ceil(approx_aim + 1/2) + 1)
    best = min(fuel_consumption_2(pos, c) for c in candidates)
    print('optimal positions:', candidates,
          'fuel consumption:', best)
