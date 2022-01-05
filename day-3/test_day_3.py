import unittest

class TestDay3(unittest.TestCase):
    diagnostics = []
    with open('test_day_3') as f:
        diagnostics = f.read().splitlines()

    def test_power_consumption(self):
        from day_3 import calculate_power_consumption
        assert calculate_power_consumption(self.diagnostics) == 198

    def test_life_support_rating(self):
        from day_3 import calculate_life_support_rating
        self.assertEqual(calculate_life_support_rating(self.diagnostics), 230 )
