import unittest
from solution import read_input, parse_submarine_commands, parse_submarine_commands_2, parse_submarine_commands_2

test_input = read_input("test_input.txt")


class TestParseSubmarineCommands(unittest.TestCase):

    def test_parse_submarine_commands(self):
        pos = parse_submarine_commands(test_input)
        self.assertEqual(pos, [15, 10])

    def test_parse_submarine_commands_2(self):
        pos = parse_submarine_commands_2(test_input)
        self.assertEqual(pos, [15, 60, 10])


if __name__ == "__main__":
    unittest.main()
