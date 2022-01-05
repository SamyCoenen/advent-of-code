import unittest
from pathlib import Path
from assertpy import assert_that
from day_5 import calculate_overlapping_points, get_points


class TestDay5(unittest.TestCase):
    points = get_points(Path('test_input'))

    def test_overlapping(self):
        assert_that(calculate_overlapping_points(self.points)).is_equal_to(12)