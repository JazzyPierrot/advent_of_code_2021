import solution as s
import unittest


class TestSegments(unittest.TestCase):

    def test_is_horizontal_or_vertical(self):
        seg = s.Segment((0, 9), (2, 9))
        self.assertEqual(seg.is_horizontal_or_vertical(), True)
        seg = s.Segment((0, 9), (0, 7))
        self.assertEqual(seg.is_horizontal_or_vertical(), True)
        seg = s.Segment((0, 9), (2, 8))
        self.assertEqual(seg.is_horizontal_or_vertical(), False)

    def test_coverage(self):
        seg = s.Segment((0, 9), (2, 9))
        seg_coverage = seg.coverage()
        self.assertEqual(next(seg_coverage), (0, 9))
        self.assertEqual(next(seg_coverage), (1, 9))
        self.assertEqual(next(seg_coverage), (2, 9))

    def test_coverage_dict(self):
        seg1 = s.Segment((0, 9), (2, 9))
        seg2 = s.Segment((0, 9), (1, 9))
        self.assertEqual(
            s.coverage_dict([seg1, seg2])[(0, 9)],
            2
        )


if __name__ == '__main__':
    unittest.main()
