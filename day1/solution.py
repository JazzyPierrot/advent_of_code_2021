def read_input(path):
    with open(path) as f:
        input = [int(line) for line in f]
    return input


def count_increase(depths):
    n_increase = [1 for i in range(len(depths) - 1)
                  if depths[i+1] - depths[i] > 0]
    return len(n_increase)


def count_increase_sliding_window(depths):
    sliding_sum = [depths[i] + depths[i+1] + depths[i+2]
                   for i in range(len(depths) - 2)]
    return count_increase(sliding_sum)


if __name__ == "__main__":
    print(f'Number of increases : {count_increase(read_input("input.txt"))}')
    print(f'Number of increases : {count_increase_sliding_window(read_input("input.txt"))}')
