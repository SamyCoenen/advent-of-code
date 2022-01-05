from collections import Counter
diagnostics = []
with open('day-3-input') as f:
    diagnostics = f.read().splitlines()

def calculate_power_consumption(diagnostics):
    gamma = int(''.join([Counter(bit).most_common(n=1)[0][0] for bit in list(zip(*diagnostics))]), 2)
    epsilon = int(len(diagnostics[0])*'1', 2) - gamma
    power_consumption = gamma*epsilon
    print(f'Gamma is: {gamma}')
    print(f'Epsilon is: {epsilon}')
    print(f'Power consumption is: {power_consumption}')
    return power_consumption

def calculate_life_support_metric(diagnostics, most_common=True):
    for i in range(len(diagnostics[0])):
        list_with_bits = [diagnostic[i] for diagnostic in diagnostics]
        common_bit_tuples = Counter(list_with_bits).most_common()
        if not most_common:
            common_bit_tuples.reverse()
        if (len(common_bit_tuples) > 1 
            and common_bit_tuples[0][1] == common_bit_tuples[1][1]):
            # True = 1, False = 0
            keep_bit = str(int(most_common))
        else:
            keep_bit = common_bit_tuples[0][0]
        diagnostics = [diagnostic for diagnostic in diagnostics
            if diagnostic[i] == keep_bit]
        if len(diagnostics) == 1:
            co2 = int(diagnostics[0], 2)
            return co2


def calculate_life_support_rating(diagnostics):
    oxygen = calculate_life_support_metric(diagnostics, most_common=True)
    co2 = calculate_life_support_metric(diagnostics, most_common=False)
    life_support_rating = co2*oxygen

    print(f'Oxygen is: {oxygen}')
    print(f'CO2 is: {co2}')
    print(f'Life support rating: {life_support_rating}')
    return life_support_rating

if __name__ == "__main__":
    calculate_power_consumption(diagnostics)
    calculate_life_support_rating(diagnostics)
