import numpy as np


class Board:
    numbers = None
    marked = None

    def __init__(self, numbers):
        num_array = np.array(numbers)
        self.numbers = num_array
        self.marked = np.zeros(num_array.shape, dtype=bool)

    def draw(self, n):
        x, y = np.where(self.numbers == n)
        if len(x) >= 1:
            self.marked[x[0], y[0]] = True

    def check(self, x, y):
        return self.marked[x, y]

    def is_complete(self):
        m = self.marked
        if (np.sum(m, 0) == m.shape[0]).any() or \
                (np.sum(m, 1) == m.shape[1]).any():
            return True
        return False

    def score(self, last_number):
        unmarked = np.extract(np.logical_not(self.marked), self.numbers)
        return np.sum(unmarked) * last_number


def read_board(f):
    board_array = []
    line = f.readline()
    while len(line.strip()) > 0:
        board_array.append([int(n) for n in line.strip().split(' ')
                            if n != ''])
        line = f.readline()
    return line, Board(board_array)


def read_input(path):
    with open(path) as f:
        boards = []
        drawn_numbers = f.readline().strip()
        drawn_numbers = [int(n) for n in drawn_numbers.split(',')]
        line = f.readline()
        while line:
            line, board = read_board(f)
            boards.append(board)
    return drawn_numbers, boards


def score_of_first_completed(drawn_numbers, boards):
    for n in drawn_numbers:
        for board in boards:
            board.draw(n)
            if board.is_complete():
                return(board.score(n))


def score_of_last_completed(drawn_numbers, boards):
    completed = [0] * len(boards)
    for n in drawn_numbers:
        for i_board, board in enumerate(boards):
            if not completed[i_board]:
                board.draw(n)
                if board.is_complete():
                    completed[i_board] = 1
                    if sum(completed) == len(boards):
                        return board.score(n)


if __name__ == "__main__":
    path = 'input.txt'
    drawn_numbers, boards = read_input(path)
    print('first score:', score_of_first_completed(drawn_numbers, boards))
    print('last score:', score_of_last_completed(drawn_numbers, boards))
