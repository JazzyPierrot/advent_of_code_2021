import unittest
from solution import count_increase, count_increase_sliding_window

test_array = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


class TestCountIncrease(unittest.TestCase):

    def test_count_increase(self):
        self.assertEqual(
            count_increase(test_array),
            7
            )


    def test_count_increase_sliding_window(self):
        self.assertEqual(
            count_increase_sliding_window(test_array),
            5
            )


if __name__ == '__main__':
    unittest.main()
