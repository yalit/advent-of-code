import math
from collections import deque

directions = [(1, 0), (-1, 0), (0 , 1), (0, -1), (0, 0)]
w = '><^v'


def bfs(start, targets, winds, width, height, lcm, shift = 0):
    to_visit = deque([(start[0], start[1], 0)])
    visited = set()
    round_trips = 0
    start = start
    target = targets[round_trips]

    while to_visit:
        x, y, nb_moves = to_visit.pop()
        nb_moves += 1

        found = False
        for dx, dy in directions:
            n_x, n_y = x + dx, y + dy

            if (n_x, n_y) == target:
                if round_trips < len(targets) - 1:
                    start = target
                    round_trips +=1
                    target = targets[round_trips]
                    visited = set()
                    to_visit = deque([(start[0], start[1], nb_moves)])
                else:
                    found = True
                    break

            if (n_x < 0 or n_y < 0 or n_x >= width or n_y >= height) and (n_x, n_y) not in targets:
                continue

            failed = False
            if (n_x, n_y) != start:
                for i, wr, wy in [(0, 1, 0), (1, -1, 0), (2, 0, -1), (3, 0, 1)]:
                    if ((n_x - (wr * (nb_moves - shift))) % width, (n_y - (wy * (nb_moves - shift))) % height) in winds[i]:
                        failed = True
                        break

            if not failed:
                k = (n_x, n_y, nb_moves % lcm)

                if k in visited:
                    continue

                visited.add(k)
                to_visit.appendleft((n_x, n_y, nb_moves))

        if found:
            break

    return nb_moves


def handle_part_1(lines: list[str]) -> int:
    winds = [set() for _ in range(4)]
    start = (0, -1)
    for y, line in enumerate(lines[1:-1]):
        for x, a in enumerate(line[1:-1]):
            if a == '.':
                continue
            winds[w.find(a)].add((x, y))
    target = (x, y + 1)
    height = y + 1
    width = x + 1

    lcm = width * height // math.gcd(width, height)

    return bfs(start, [target], winds, width, height, lcm)


def handle_part_2(lines: list[str]) -> int:
    winds = [set() for _ in range(4)]
    start = (0, -1)
    for y, line in enumerate(lines[1:-1]):
        for x, a in enumerate(line[1:-1]):
            if a == '.':
                continue
            winds[w.find(a)].add((x, y))
    target = (x, y + 1)
    height = y + 1
    width = x + 1

    lcm = width * height // math.gcd(width, height)

    return bfs(start, [target, start, target], winds, width, height, lcm)

