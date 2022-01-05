import unittest
from itertools import chain
from pathlib import Path

import assertpy

import day_8


class TestDay8(unittest.TestCase):

    def test_calculate_central_position(self):
        signal_patterns, output = day_8.get_signals(Path('test_input_day_8'))
        print(signal_patterns)
        print(output)
        digits = day_8.reverse_engineer_digits(output)
        print(digits)
        digit_bools = [d is not None for d in chain(*digits)]
        print(sum(digit_bools))