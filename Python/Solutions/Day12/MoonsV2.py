import numpy
import functools

def read_input(file="input.txt"):
    with open(file) as file:
        lst = []
        for line in file:
            t = tuple(map(lambda e: int(e.split('=')[1]), line.strip().strip('<>').split(',')))
            lst.append(t)
        return lst


def less(l, i):
    return len(list(filter(lambda x: x < l[i], l)))


def greater(l, i):
    return len(list(filter(lambda x: x > l[i], l)))


def count(l):
    return [greater(l, i) - less(l, i) for i in range(0, len(l))]


def main():
    P = read_input()
    cycle = []
    for coord in range(0, 3):
        step = 0
        pos = [x[coord] for x in P]
        pos0 = pos.copy()
        vel = [0 for i in range(0, 4)]
        vel0 = vel.copy()
        while True:
            vel = list(map(lambda t: t[0] + t[1], zip(count(pos), vel)))
            pos = list(map(lambda t: t[0] + t[1], zip(pos, vel)))
            step = step + 1
            print(step)
            if pos0 == pos and vel0 == vel:
                cycle.append(step)
                break
    print(functools.reduce(numpy.lcm, cycle))

main()
