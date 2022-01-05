import unittest

import assertpy

import day_6


class TestDay6(unittest.TestCase):

    def test_18_days(self):
        lantern_fish_list = [3, 4, 3, 1, 2]
        lantern_fish_count = day_6.calculate_lanternfish_growth(lantern_fish_list, days=18)
        assertpy.assert_that(lantern_fish_count).is_equal_to(26)
