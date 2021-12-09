import itertools


def read_line(line):
    signal_patterns, output = line.strip().split(' | ')
    signal_patterns = signal_patterns.split(' ')
    output = output.split(' ')
    return signal_patterns, output


def read_input(path):
    with open(path) as f:
        res = [read_line(line) for line in f]
    return res


seg_to_digit = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def translate(mapping, code):
    code_translated = code.translate(str.maketrans(''.join(all_letters),
                                                   ''.join(mapping)))
    return ''.join(sorted(code_translated))


def check_if_valid(mapping, codes):
    valid_code = [translate(mapping, c) in seg_to_digit for c in codes]
    return all(valid_code)


def test_permutations(codes):
    # brute force
    n = 0
    for mapping in itertools.permutations(all_letters):
        n += 1
        ok = check_if_valid(mapping, codes)
        if ok:
            return mapping
    print(n)


if __name__ == '__main__':
    path = 'input.txt'
    n1478 = 0
    for input in read_input(path):
        n1478 += len([c for c in input[1] if len(c) in [2, 4, 3, 7]])
    print(n1478)

    n = 0
    for input in read_input(path):
        mapping = test_permutations(input[0] + input[1])
        num_out = 0
        for code in input[1]:
            num_out = num_out * 10 + seg_to_digit[translate(mapping, code)]
        n += num_out
    print(n)
