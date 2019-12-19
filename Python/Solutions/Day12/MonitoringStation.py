class Moon:
    pos = (0, 0, 0)
    velocity = (0, 0, 0)

    def __init__(self, x, y, z):
        self.pos = (x, y, z)

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

prev_pos = []

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
    while True:
        prev_pos.append([[moon.pos for moon in moons], [moon.velocity for moon in moons]])
        for moon1 in moons:
            for moon2 in moons:
                if moon1 != moon2:
                    moon1.apply_gravity(moon2)
        for moon in moons:
            moon.apply_velocity()
        t = t + 1
        if [[moon.pos for moon in moons], [moon.velocity for moon in moons]] in prev_pos:
            break
    print(t)


main()
