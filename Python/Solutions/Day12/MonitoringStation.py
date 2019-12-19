class Moon:
    prev_pos = []
    pos = (0, 0, 0)
    velocity = (0, 0, 0)

    def __init__(self, x, y, z):
        self.pos = (x, y, z)
        self.prev_pos = []

    def calc_energy(self):
        pot_energy = sum(list(map(lambda x: abs(x), self.pos)))
        kin_energy = sum(list(map(lambda x: abs(x), self.velocity)))
        return pot_energy * kin_energy

    def velocity_change(self, a, b):
        if a > b:
            return -1
        elif a < b:
            return 1
        else:
            return 0

    def apply_gravity(self, moon):
        self.velocity = tuple(map(lambda t: t[2] + self.velocity_change(t[0], t[1]), zip(self.pos, moon.pos, self.velocity)))

    def apply_velocity(self):
        self.pos = tuple(map(lambda t: t[0] + t[1], zip(self.pos, self.velocity)))


def read_input(file="input.txt"):
    with open(file) as file:
        lst = []
        for line in file:
            t = tuple(map(lambda e: int(e.split('=')[1]), line.strip().strip('<>').split(',')))
            lst.append(Moon(*t))
        return lst


def main():
    moons = read_input()
    equal = False
    t = 0
    while not equal:
        for moon1 in moons:
            moon1.prev_pos.append(moon1.pos)
        for moon1 in moons:
            for moon2 in moons:
                if moon1 != moon2:
                    moon1.apply_gravity(moon2)
        for moon in moons:
            moon.apply_velocity()
        equal = True
        for moon in moons:
            if moon.pos not in moon.prev_pos:
                equal = False
                break
        t = t + 1
        print(t)
    energy = 0
    for moon in moons:
        energy = energy + moon.calc_energy()
    print(t-1)


main()
