from collections import deque
from pathlib import Path

from more_itertools import locate


def calculate_lanternfish_growth(lantern_fish_list, days):
    lantern_fish_counts_list = deque(list(map(lambda c: lantern_fish_list.count(c), range(9))))
    for day in range(days):
        new_births = lantern_fish_counts_list.popleft()
        lantern_fish_counts_list[6] += new_births
        lantern_fish_counts_list.append(new_births)
    return sum(lantern_fish_counts_list)


if __name__ == '__main__':
    file = Path('day-6-input')
    lantern_fish_list = list(map(int, file.read_text().strip().split(',')))
    print(calculate_lanternfish_growth(lantern_fish_list, days=80))
    print(calculate_lanternfish_growth(lantern_fish_list, days=256))