import sys


def handle_part_1(lines: list[str]) -> int:
    orbits = {}

    for line in lines:
        [l, r] = line.split(')')
        if r not in orbits:
            orbits[r] = []
        orbits[r].append(l)

    nb_orbits = 0
    for planet in orbits.keys():
        to_visit = orbits[planet][:]

        while len(to_visit) > 0:
            next_planet = to_visit.pop()
            nb_orbits += 1
            if next_planet != 'COM':
                to_visit += orbits[next_planet]

    return nb_orbits


def handle_part_2(lines: list[str]) -> int:
    orbits = {}

    for line in lines:
        [l, r] = line.split(')')
        if r not in orbits:
            orbits[r] = {'orbits': [], 'orbited_by': []}
        if l not in orbits:
            orbits[l] = {'orbits': [], 'orbited_by': []}
        orbits[r]['orbits'].append(l)
        orbits[l]['orbited_by'].append(r)


    source = 'YOU'
    min_dist = {x: sys.maxsize for x in orbits.keys()}
    min_dist[source] = 0
    previous_planets = {}
    unvisited_planets = list(orbits.keys())

    while unvisited_planets:
        c_min_planet = None
        for planet in unvisited_planets:  # Iterate over the nodes
            if c_min_planet is None:
                c_min_planet = planet
            elif min_dist[planet] < min_dist[c_min_planet]:
                c_min_planet = planet

        around_planets = orbits[c_min_planet]['orbits'] + orbits[c_min_planet]['orbited_by']
        for planet in around_planets:
            dist = min_dist[c_min_planet] + 1
            if dist < min_dist[planet]:
                min_dist[planet] = dist
                previous_planets[planet] = c_min_planet

        unvisited_planets.remove(c_min_planet)

    return min_dist['SAN'] - 2
