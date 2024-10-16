import math
from typing import Tuple, List, Set

from python.libraries.utils import euclidian_distance


def handle_part_1(lines: list[str]) -> int:
    asteroids = get_asteroids(lines)

    data = []
    for x,y in asteroids:
        seen = get_seen(asteroids, x, y)
        data.append((len(seen), (x, y), seen))

    return sorted(data, key=lambda x: x[0], reverse=True)[0][0]


def handle_part_2(lines: list[str]) -> int:
    asteroids = get_asteroids(lines)

    data = []
    for x, y in asteroids:
        seen = get_seen(asteroids, x, y)
        data.append((len(seen), (x, y), seen))

    base_data = sorted(data, key=lambda x: x[0], reverse=True)[0]
    bx, by = base_data[1]

    v = 0
    while v < 200:
        for _, _, target in get_seen(asteroids, bx, by):
            asteroids.remove((target[0], target[1]))
            v+=1
            if v == 200:
                return target

def get_asteroids(lines: list[str]) -> Set[Tuple[int, int]]:
    grid = [list(x) for x in lines]
    h = len(lines)
    w = len(grid[0])

    asteroids = set()
    for x in range(w):
        for y in range(h):
            if grid[y][x] == '.':
                continue
            asteroids.add((x, y))
    return asteroids

def get_seen(asteroids, x, y) -> List[Tuple[int, Tuple[int, int]]]:
    seen = {}
    for tx, ty in asteroids:
        if tx == x and ty == y:
            continue

        if tx == x:
            slope = "up" if ty < y else "down"
        elif ty == y:
            slope = "left" if tx < x else "right"
        else:
            slope = ("right" if tx > x else "left", (ty-y)/(tx-x))

        if slope not in seen:
            seen[slope] = []
        seen[slope].append((euclidian_distance((tx,ty), (x,y)), (tx, ty)))

    targets = []
    for slope in seen:
        tx, ty = sorted(seen[slope])[0][1]
        targets.append((get_angle(x, y, tx, ty), slope[1], (tx, ty)))
    return sorted(targets)

def get_angle(x_0, y_0, x_1, y_1):
    x = abs(x_1 - x_0)
    y = abs(y_1 - y_0)
    angle = math.degrees(math.acos(y/math.sqrt(x**2+y**2)))

    if x_1 >= x_0 and y_1 < y_0:
        return angle
    elif x_1 > x_0 and y_1 >= y_0:
        return 180 -angle
    elif x_1 <= x_0 and y_1 > y_0:
        return 180 + angle
    else:
        return 360 - angle