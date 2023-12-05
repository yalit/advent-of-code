import unittest

from python.libraries.utils import merge_ranges, intersect_range


class TestUtils(unittest.TestCase):
    def test_merge_ranges_same(self):
        ranges = [(1,2), (3,4)]
        merged_ranges = merge_ranges(ranges)
        assert ranges == merged_ranges

    def test_merge_ranges_reversed(self):
        ranges = [(3,4), (1,2)]
        merged_ranges = merge_ranges(ranges)
        assert [(1,2), (3,4)] == merged_ranges

    def test_merge_ranges_overlapping(self):
        ranges = [(1,4), (3,4), (2,5), (7, 10)]
        merged_ranges = merge_ranges(ranges)
        assert [(1, 5), (7, 10)] == merged_ranges


    def test_intersect_ranges_outside(self):
        intersect = intersect_range((1,2), (3,6))
        assert None == intersect

        intersect = intersect_range((7, 8), (3, 6))
        assert None == intersect

    def test_intersect_around_start(self):
        intersect = intersect_range((1, 5), (3, 6))
        assert (3,5) == intersect

        intersect = intersect_range((1, 7), (3, 6))
        assert (3, 6) == intersect

    def test_intersect_around_end(self):
        intersect = intersect_range((4, 7), (3, 6))
        assert (4,6) == intersect

        intersect = intersect_range((4,5), (3, 6))
        assert (4,5) == intersect

    def test_intersect_around_fully(self):
        intersect = intersect_range((2, 8), (3, 6))
        assert (3,6) == intersect

if __name__ == "__main__":
    unittest.main()
