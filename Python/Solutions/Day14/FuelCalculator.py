import math
from collections import defaultdict


def sanitize_input(filename='input.txt'):
    production_rules = {}
    with open(filename) as file:
        for line in file:
            from_to = line.split("=>")
            ingredients = from_to[0].strip().split(",")
            ingredients = {x.split()[1]: int(x.split()[0]) for x in ingredients}
            (result_count, result_ingredient) = from_to[1].strip().split()
            production_rules[result_ingredient] = (int(result_count), ingredients)

    return production_rules


def calc_ore_needs(result, result_count, production_rules, spare):
    (count, ingredients) = production_rules[result]
    rule_mult = math.ceil(result_count / count)
    if "ORE" in ingredients:
        spare[result] = spare[result] + (rule_mult * count) - result_count
        return rule_mult * ingredients["ORE"]

    ore_count = 0
    for ingredient in ingredients:
        amount = ingredients[ingredient] * rule_mult - spare[ingredient]
        spare[ingredient] = abs(amount) if amount < 0 else 0
        if amount < 0:
            continue
        ore_count = ore_count + calc_ore_needs(ingredient, amount, production_rules, spare)

    spare[result] = spare[result] + (rule_mult * count) - result_count
    return ore_count


def part1(filename='input.txt'):
    rules = sanitize_input(filename)
    print(calc_ore_needs("FUEL", 1, rules, defaultdict(lambda: 0)))

def part2(filename='input.txt'):
    rules = sanitize_input(filename)
    ore_count = 1000000000000
    spare = defaultdict(lambda: 0)

    i = 0
    while i <= 0 or len([value for key, value in spare.items() if value > 0]) > 0:
        ore_needs = calc_ore_needs("FUEL", 1, rules, spare)
        ore_count = ore_count - ore_needs
        print(ore_count)
        i = i + 1

    print(i)


part2()
