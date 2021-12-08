import numpy as np
import itertools as it
import math


class Segment:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.coor = (end[0] - start[0], end[1] - start[1])

    def is_horizontal(self):
        return self.start[0] == self.end[0]

    def is_vertical(self):
        return self.start[1] == self.end[1]

    def is_horizontal_or_vertical(self):
        return self.is_horizontal() or self.is_vertical()

    def coverage(self):
        horizontal_range = range(
            self.start[0],
            self.end[0] + int(math.copysign(1, self.coor[0])),
            int(math.copysign(1, self.coor[0]))
        )
        vertical_range = range(
            self.start[1],
            self.end[1] + int(math.copysign(1, self.coor[1])),
            int(math.copysign(1, self.coor[1]))
        )
        if self.is_horizontal():
            for pos in zip(it.cycle([self.start[0]]), vertical_range):
                yield pos
        elif self.is_vertical():
            for pos in zip(horizontal_range, it.cycle([self.start[1]])):
                yield pos
        else:
            for pos in zip(horizontal_range, vertical_range):
                yield pos


def read_segment(line):
    start, end = line.split(' -> ')
    start = [int(n) for n in start.split(',')]
    end = [int(n) for n in end.split(',')]
    return Segment(start, end)


def read_input(path, filter_hv):
    with open(path) as f:
        segments = [read_segment(line.strip()) for line in f]
    if filter_hv:
        segments = [seg for seg in segments
                    if seg.is_horizontal_or_vertical()]
    return segments


def coverage_dict(segments):
    coverage = {}
    for seg in segments:
        for pos in seg.coverage():
            if pos not in coverage:
                coverage[pos] = 1
            else:
                coverage[pos] += 1
    return coverage


if __name__ == '__main__':
    path = 'input.txt'
    segments = read_input(path, True)
    print(len([n for k, n in coverage_dict(segments).items() if n >= 2]))
    segments = read_input(path, False)
    print(len([n for k, n in coverage_dict(segments).items() if n >= 2]))
