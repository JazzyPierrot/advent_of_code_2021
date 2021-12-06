
def parse_line(line):
    splitted = str.split(line, " ")
    return (splitted[0], int(splitted[1]))


def read_input(path):
    with open(path) as f:
        input = [parse_line(line) for line in f]
    return input


def go_forward(position, amount):
    position[0] += amount
    return position


def go_up(position, amount):
    position[1] -= amount
    return position


def go_down(position, amount):
    position[1] += amount
    return position


def parse_submarine_command(command, position, command_dict):
    action_fun = command_dict.get(command[0], lambda x, y: 1/0)
    amount = command[1]
    return action_fun(position, amount)


command_dict_1 = {
        "forward": go_forward,
        "up": go_up,
        "down": go_down
        }


def parse_submarine_commands(commands):
    position = [0, 0]
    for command in commands:
        position = parse_submarine_command(command, position, command_dict_1)
    return position


def aim_up(position, amount):
    position[2] -= amount
    return position


def aim_down(position, amount):
    position[2] += amount
    return position


def aim_forward(position, amount):
    position = go_forward(position, amount)
    position[1] += amount * position[2]
    return position


command_dict_2 = {
        "forward": aim_forward,
        "up": aim_up,
        "down": aim_down
        }


def parse_submarine_commands_2(commands):
    position = [0, 0, 0]
    for command in commands:
        position = parse_submarine_command(command, position, command_dict_2)
    return position


if __name__ == "__main__":
    result1 = parse_submarine_commands(read_input("input.txt"))
    print(f'final position: {result1}, product: {result1[0] * result1[1]}')

    result2 = parse_submarine_commands_2(read_input("input.txt"))
    print(f'final position: {result2}, product: {result2[0] * result2[1]}')
