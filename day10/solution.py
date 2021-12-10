import queue
import statistics


def read_input(path):
    with open(path) as f:
        return [line.strip() for line in f]


opening = '([{<'
closing = ')]}>'

penalty = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def matching(opening):
    for pair in ['()', '[]', '{}', '<>']:
        if opening == pair[0]:
            return pair[1]


def matches(opening, closing):
    return closing == matching(opening)


def check_corruption(subsystem):
    lifo = queue.LifoQueue()
    for c in subsystem:
        if c in opening:
            lifo.put(c)
        if c in closing:
            last_open = lifo.get()
            if not matches(last_open, c):
                return c, []
    unclosed = []
    while lifo.qsize() > 0:
        unclosed.append(lifo.get())
    return None, [matching(c) for c in unclosed]


points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def score_completion(completion):
    score = 0
    for c in completion:
        score *= 5
        score += points[c]
    return score


if __name__ == "__main__":
    path = 'input.txt'
    nav_system = read_input(path)
    pen = 0
    scores = []
    for subsystem in nav_system:
        corr, completion = check_corruption(subsystem)
        if corr is not None:
            pen += penalty[corr]
        else:
            scores.append(score_completion(completion))

    print(pen)
    print(statistics.median(scores))
