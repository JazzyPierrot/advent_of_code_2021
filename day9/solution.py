class Point:

    def __init__(self, height, x, y):
        self.x = x
        self.y = y
        self.height = height
        self.basin_low_point = None


class Points:

    max_x = 0
    max_y = 0
    points = []

    def __init__(self, points):
        self.points = points
        self.max_x = len(points)
        self.max_y = len(points[0])

    def neighbors(self, x, y):
        neighbors = []
        if x > 0:
            neighbors.append(self.points[x-1][y])
        if y > 0:
            neighbors.append(self.points[x][y-1])
        if x < self.max_x - 1:
            neighbors.append(self.points[x+1][y])
        if y < self.max_y - 1:
            neighbors.append(self.points[x][y+1])
        return neighbors

    def get_low_points(self):
        low_points = []
        for x, line in enumerate(self.points):
            for y, point in enumerate(line):
                neighbor_h = [n.height for n in self.neighbors(x, y)]
                if all([nh > point.height for nh in neighbor_h]):
                    low_points.append(point)
                    point.basin_low_point = point
        return low_points

    def tag_basins(self, low_point):
        for n in self.neighbors(low_point.x, low_point.y):
            if n.height < 9 and n.basin_low_point is None:
                n.basin_low_point = low_point.basin_low_point
                self.tag_basins(n)

    def count_basins(self):
        counts = {}
        for line in self.points:
            for point in line:
                basin = point.basin_low_point
                if basin is not None:
                    if basin in counts:
                        counts[basin] += 1
                    else:
                        counts[basin] = 1
        return counts


def read_line(line, x):
    n = len(line)
    return [Point(int(h), x, y) for h, y in zip([c for c in line], range(n))]


def read_points(path):
    with open(path) as f:
        lines = f.readlines()
    n = len(lines)
    return Points([read_line(ln.strip(), x) for ln, x in zip(lines, range(n))])


if __name__ == '__main__':
    path = 'input.txt'
    points = read_points(path)
    lp = points.get_low_points()
    print(sum([p.height + 1 for p in lp]))

    for low_point in lp:
        points.tag_basins(low_point)
    print(sorted(points.count_basins().values()))
