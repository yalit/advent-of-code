import math
from typing import Tuple, List

from sympy.physics.units import velocity


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


def get_next_position(planets: List[int], velocity: List[int]) -> Tuple[List[int], List[int]]:
    new_planets = planets[:]
    new_velocities = velocity[:]
    for a in range(len(planets)):
        for b in range(len(planets)):
            if a == b:
                continue

            if planets[a] < planets[b]:
                new_velocities[a] += 1
            elif planets[a] > planets[b]:
                new_velocities[a] -= 1
        new_planets[a] += new_velocities[a]

    return new_planets, new_velocities

def handle_part_2(lines: list[str]) -> int:
    planets = get_planets(lines)
    original_planet_x, planet_x = [p[0] for p in planets], [p[0] for p in planets]
    original_planet_y, planet_y = [p[1] for p in planets], [p[1] for p in planets]
    original_planet_z, planet_z = [p[2] for p in planets], [p[2] for p in planets]

    original_velocity_x, velocity_x = [0 for _ in planets], [0 for _ in planets]
    original_velocity_y, velocity_y = [0 for _ in planets], [0 for _ in planets]
    original_velocity_z, velocity_z = [0 for _ in planets], [0 for _ in planets]

    step_x, step_y, step_z = 1, 1, 1

    planet_x, velocity_x = get_next_position(planet_x, velocity_x)
    planet_y, velocity_y = get_next_position(planet_y, velocity_y)
    planet_z, velocity_z = get_next_position(planet_z, velocity_z)

    while not (planet_x == original_planet_x and velocity_x == original_velocity_x):
        planet_x, velocity_x = get_next_position(planet_x, velocity_x)
        step_x += 1

    while not (planet_y == original_planet_y and velocity_y == original_velocity_y):
        planet_y, velocity_y = get_next_position(planet_y, velocity_y)
        step_y += 1

    while not (planet_z == original_planet_z and velocity_z == original_velocity_z):
        planet_z, velocity_z = get_next_position(planet_z, velocity_z)
        step_z += 1

    return math.lcm(step_x, math.lcm(step_y, step_z))
