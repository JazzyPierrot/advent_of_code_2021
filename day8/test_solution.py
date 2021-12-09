import unittest
import solution as s


class TestOptions(unittest.TestCase):

    def test_options(self):
        options = s.restrict_options(['cde', 'de'])
        self.assertEqual(options['c'], {'a'})

    def test_translate(self):
        self.assertEqual(s.translate(
            ('c', 'b', 'a', 'd', 'e', 'f', 'g'), 'abc'), 'abc')

    def test_validity(self):
        self.assertEqual(
            s.check_if_valid(('c', 'f', 'g', 'a', 'b', 'd', 'e'), ['cagedb']),
            True
        )


if __name__ == '__main__':
    unittest.main()
