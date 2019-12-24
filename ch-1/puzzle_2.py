from math import floor


def calculate_fuel(fuel):
    if fuel <= 0:
        return 0
    new_fuel = int(floor(fuel/3-2))
    return calculate_fuel(new_fuel) + fuel


f = open("input_test", "r")
result = 0

for line in f:
    mass = int(line.strip())
    result += calculate_fuel(floor(mass/3-2))

f.close()
print(int(result))
