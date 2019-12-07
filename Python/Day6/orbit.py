def orbitals(m, point):
    if point in m:
        orbit_point = m[point]
        return 1 + orbitals(m, orbit_point)
    else:
        return 0


def orbitals_sum(m):
    return sum([orbitals(m, x) for x in m.keys()])


def orbitals_map(file_name="input.txt"):
    m = {}
    with open(file_name) as file:
        for line in file:
            X = line.strip().split(")")
            orbiter = X[1]
            orbit_point = X[0]

            m[orbiter] = orbit_point

    return m


print(orbitals_sum(orbitals_map()))
