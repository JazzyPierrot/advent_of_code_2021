import unittest
import solution as s


class TestDraw(unittest.TestCase):

    def test_draw(self):
        board = s.Board([[1, 2], [3, 4]])
        board.draw(3)
        self.assertEqual(board.check(1, 0), True)
        self.assertEqual(board.check(0, 0), False)

    def test_complete(self):
        board = s.Board([[1, 2], [3, 4]])
        board.draw(3)
        self.assertEqual(board.is_complete(), False)
        board.draw(4)
        self.assertEqual(board.is_complete(), True)

    def test_score(self):
        board = s.Board([[1, 2], [3, 4]])
        last_number = 2
        self.assertEqual(board.score(last_number), 20)
        board.draw(3)
        self.assertEqual(board.score(last_number), 14)


if __name__ == "__main__":
    unittest.main()
