from itertools import chain
from pathlib import Path

patterns = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}


def get_signals(file: Path):
    lines = file.read_text().splitlines()
    signal_patterns = [signal.split(' ') for signal in [line.split('|')[0].strip() for line in lines]]
    outputs = [signal.split(' ') for signal in [line.split('|')[1].strip() for line in lines]]
    return signal_patterns, outputs


def reverse_engineer_digits(signal_patterns_list):
    return [list(map(lambda s: patterns.get(len(s)), signal_patterns)) for signal_patterns in signal_patterns_list]


if __name__ == '__main__':
    signal_patterns, output = get_signals(Path('input_day_8'))
    print(signal_patterns)
    print(output)
    digits = reverse_engineer_digits(output)
    print(digits)
    digit_bools = [d is not None for d in chain(*digits)]
    print(sum(digit_bools))