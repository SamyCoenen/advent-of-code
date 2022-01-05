import unittest
from pathlib import Path

import assertpy

from day_7 import calculate_central_position, get_crab_positions

class TestDay6(unittest.TestCase):

    def test_calculate_central_position(self):
        central_position, total_fuel = calculate_central_position(get_crab_positions(Path('test_input_day_7')), part2=False)
        assertpy.assert_that(central_position,).is_equal_to(2)
        assertpy.assert_that(total_fuel).is_equal_to(37)

    def test_calculate_central_position2(self):
        central_position, total_fuel = calculate_central_position(get_crab_positions(Path('test_input_day_7')), part2=True)
        assertpy.assert_that(central_position,).is_equal_to(5)
        assertpy.assert_that(total_fuel).is_equal_to(168)
