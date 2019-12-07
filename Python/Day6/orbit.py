from operator import itemgetter


def orbitals(m, point):
    if point in m:
        orbit_point = m[point]
        l = [orbit_point]
        l.extend(orbitals(m, orbit_point))
        return l
    else:
        return []


def orbitals_sum(m):
    return sum([len(orbitals(m, x)) for x in m.keys()])


def orbitals_intersect(m, p1, p2):
    l1 = orbitals(m, p1)
    l2 = orbitals(m, p2)
    return [x for x in l1 if x in l2]


def closest_orbital_intersect(m, p1, p2):
    intersect = orbitals_intersect(m, p1, p2)
    z = zip(intersect, [len(orbitals(m, x)) for x in intersect])
    return max(z, key=itemgetter(1))[0]


def orbitals_path_length(m, p1, p2):
    closest_intersection = closest_orbital_intersect(m, p1, p2)
    intersection_len = len(orbitals(m, closest_intersection))
    return len(orbitals(m, p1)) - intersection_len + len(orbitals(m, p2)) - intersection_len


def orbitals_map(file_name="input.txt"):
    m = {}
    with open(file_name) as file:
        for line in file:
            X = line.strip().split(")")
            orbiter = X[1]
            orbit_point = X[0]

            m[orbiter] = orbit_point

    return m


print(orbitals_path_length(orbitals_map(), "YOU", "SAN") - 2)
