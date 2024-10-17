from typing import Tuple


def get_planets(lines: list[str])->list[Tuple[int, int, int]]:
    planets = []

    for line in lines:
        coordinates = line[1:-1].split(', ')
        planets.append((int(coordinates[0].split("=")[1]), int(coordinates[1].split("=")[1]), int(coordinates[2].split("=")[1])))

    return planets

def get_delta_velocity(p1, p2)-> int:
    if p1 > p2:
        return -1
    elif p1 < p2:
        return 1
    else:
        return 0

def handle_part_1(lines: list[str]) -> int:
    planets = get_planets(lines)
    velocities = [(0,0,0) for _ in planets]

    for _ in range(1000):
        new_planets = [(0,0,0) for p in planets]
        for i, planet in enumerate(planets):
            for second_planet in planets:
                if second_planet == planet:
                    continue

                velocities[i] = (
                    velocities[i][0] + get_delta_velocity(planet[0], second_planet[0]),
                    velocities[i][1] + get_delta_velocity(planet[1], second_planet[1]),
                    velocities[i][2] + get_delta_velocity(planet[2], second_planet[2])
                )
            new_planets[i] = (planet[0] + velocities[i][0], planet[1] + velocities[i][1], planet[2] + velocities[i][2])
        planets = new_planets

    potential = [sum(map(abs, p)) for p in planets]
    kinetic = [sum(map(abs, v)) for v in velocities]

    return sum([p*v for p,v in zip(potential, kinetic)])


def handle_part_2(lines: list[str]) -> int:
    return 0
