import unittest
from pathlib import Path

from day_4 import calculate_score, is_row_filled, is_column_filled


# numbers = [7 ,4 ,9 ,5 ,11 ,17 ,23 ,2 ,0 ,14 ,21 ,24 ,10 ,16 ,13 ,6 ,15 ,25 ,12 ,22 ,18 ,20 ,8 ,19 ,3 ,26 ,1]
# boards = [
#     [[22, 13, 17, 11,  0],
#     [8,  2, 23,  4, 24],
#     [21,  9, 14, 16,  7],
#     [6, 10,  3, 18,  5],
#     [1, 12, 20, 15, 19]],
#
#     [[3, 15,  0,  2, 22],
#     [9, 18, 13, 17,  5],
#     [19,  8,  7, 25, 23],
#     [20, 11, 10, 24,  4],
#     [14, 21, 16, 12,  6]],
#
#     [[14, 21, 17, 24,  4],
#     [10, 16, 15,  9, 19],
#     [18,  8, 23, 26, 20],
#     [22, 11, 13,  6,  5],
#     [ 2,  0, 12,  3,  7]]
# ]


class TestDay4(unittest.TestCase):
    from day_4 import load_data
    numbers, boards = load_data(Path('test-input-4'))

    def test_numbers_loaded(self):
        self.assertEqual(len(self.boards), 3)
        self.assertEqual([7, 4, 9, 5, 11], self.numbers[:5])

    def test_score_win(self):
        self.assertEqual(calculate_score(self.numbers, self.boards), 4512)

    def test_score_lose(self):
        self.assertEqual(calculate_score(self.numbers, self.boards, choose_win=False), 1924)

    def test_is_row_filled(self):
        r = is_row_filled(drawn_numbers=[22, 13, 17, 11, 0], boards=self.boards)[0]
        self.assertTrue(r == 0)

    def test_is_column_filled(self):
        r = is_column_filled(drawn_numbers=[3,9,19,20,14], boards=self.boards)[0]
        self.assertTrue(r == 1)