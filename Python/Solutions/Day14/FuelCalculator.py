def sanitize_input(filename='input.txt'):
    production_rules = {}
    with open(filename) as file:
        for line in file:
            from_to = line.split("=>")
            ingredients = from_to[0].strip().split(",")
            ingredients = {x.split()[1] : int(x.split()[0]) for x in ingredients}
            (result_count, result_ingredient) = from_to[1].strip().split()
            production_rules[result_ingredient] = (result_count, ingredients)

    return production_rules

def calc_ore_needs(result, result_count, production_rules):
    (count, ingredients) = production_rules[result]
    # TODO return number of ores needed to produce result_count results

    # if only ores needed for result return ores
    # else
    # TODO: ongeveer zoiets:
    # ores needed = result_count / count * sum over ingredients : ingredient_count * calc_ore_needs(ingredient, production_rules)
    pass

def part1(filename='input.txt'):
    print(sanitize_input(filename))


part1()
