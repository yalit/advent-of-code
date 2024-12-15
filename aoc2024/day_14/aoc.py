import re
from functools import reduce

from python.libraries.array import visualize


def get_pos_after(x, y, vx, vy, w, h, n):
    nx, ny = (x + n * vx), (y + n * vy)
    if nx > 0:
        nx = nx % w
    else:
        nx = nx - (nx // w * w)

    if ny > 0:
        ny = ny % h
    else:
        ny = ny - (ny // h * h)

    return nx, ny


def dist(x, y, nx, ny):
    return abs(nx - x) + abs(ny - y)


def handle_part_1(lines: list[str]) -> int:
    w, h = list(map(int, lines[0].split()))

    robots = []
    for line in lines[1:]:
        x, y, vx, vy = list(
            map(int, re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups())
        )

        robots.append((x, y, vx, vy))

    quadrants = [0, 0, 0, 0]
    for x, y, vx, vy in robots:
        nx, ny = get_pos_after(x, y, vx, vy, w, h, 100)
        if nx < w // 2 and ny < h // 2:
            quadrants[0] += 1
        elif nx < w // 2 and ny > h // 2:
            quadrants[2] += 1
        elif nx > w // 2 and ny < h // 2:
            quadrants[1] += 1
        elif nx > w // 2 and ny > h // 2:
            quadrants[3] += 1

    return reduce(lambda m, e: m * e, quadrants, 1)


def handle_part_2(lines: list[str]) -> int:
    w, h = list(map(int, lines[0].split()))

    robots = []
    for line in lines[1:]:
        x, y, vx, vy = list(
            map(int, re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups())
        )

        robots.append((x, y, vx, vy))

    i = 0
    while True:
        grid = [["." for _ in range(w)] for _ in range(h)]
        for x, y, vx, vy in robots:
            nx, ny = get_pos_after(x, y, vx, vy, w, h, i)
            grid[ny][nx] = "X"

        n = sum(len([x for x in row if x == "X"]) for row in grid)
        i += 1
        if n == len(robots):
            break

    print(f"--------{i} seconds----------------")
    visualize(grid)
    return i - 1
