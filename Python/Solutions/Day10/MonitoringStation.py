import math


def common_divs(a, b):
    return [i for i in range(2, min(a, b) + 1) if a % i == b % i == 0]


def parse_input():
    with open("input.txt") as file:
        lst = []
        coordinates = []
        i = 0
        for line in file:
            lst.append(list(line.strip()))
            i = i + 1
        for j in range(0, i):
            for k in range(0, len(lst[0])):
                if lst[j][k] == "#":
                    coordinates.append((k, j))
        return coordinates


def intermediate_coordinates(a, b):
    width = abs(a[0] - b[0])
    height = abs(a[1] - b[1])

    w_sign = 1 if b[0] - a[0] > 0 else -1
    h_sign = 1 if b[1] - a[1] > 0 else -1

    if width == 0:
        return [(a[0], a[1] + h_sign * i) for i in range(1, height)]
    elif height == 0:
        return [(a[0] + w_sign * i, a[1]) for i in range(1, width)]
    else:
        divs = common_divs(width, height)
        inter = [[(round(w_sign * j * width / i + a[0]), round(h_sign * j * height / i + a[1])) for j in range(1, i)] for i in divs]
        return [item for sublist in inter for item in sublist]


def visible_astroids(p, coordinates):
    count = 0
    for coordinate in coordinates:
        if coordinate == p:
            continue

        inters = intermediate_coordinates(p, coordinate)
        found = False
        for inter in inters:
            if inter in coordinates:
                found = True
                break
        if not found:
            count = count + 1
    return count


def main():
    coordinates = parse_input()
    print(list(zip(coordinates, [visible_astroids(p, coordinates) for p in coordinates])))
    print(max([visible_astroids(p, coordinates) for p in coordinates]))


main()
