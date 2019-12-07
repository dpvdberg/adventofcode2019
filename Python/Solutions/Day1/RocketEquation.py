import math


def calc_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel(fuel)


s = 0
with open("input.txt") as file:
    for x in file:
        s = s + calc_fuel(int(x))
    print(s)
