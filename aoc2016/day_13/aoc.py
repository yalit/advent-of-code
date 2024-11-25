from queue import PriorityQueue
from threading import currentThread
from python.libraries.utils import directNeighbors

graph = {}


def bfs(start, target, seed):
    to_visit = [(start, 0, [])]
    visited = set()

    while to_visit:
        current, steps, path = to_visit.pop(0)

        if current in visited:
            continue

        if current == target:
            # display_path(path + [current])
            return steps

        for n in get_neighbors(current, seed):
            to_visit.append((n, steps + 1, path + [current]))
        visited.add(current)

    return -1


def is_wall(seed: int, x: int, y: int):
    c = x**2 + 3 * x + 2 * x * y + y + y**2
    c += seed
    ones = sum(list(map(int, bin(c)[2:])))
    return ones % 2 == 1


def heuristic(pos, target):
    return abs(target[0] - pos[0]) + abs(target[1] - pos[1])


def get_neighbors(pos, seed):
    for dx, dy in directNeighbors:
        x, y = (pos[0] + dx, pos[1] + dy)
        if x < 0 or y < 0:
            continue
        if is_wall(seed, x, y):
            graph[(x, y)] = "#"
            continue

        graph[(x, y)] = "."
        yield (x, y)


def display_path(path):
    for p in path:
        graph[p] = "O"
    graph[path[0]] = "S"
    graph[path[-1]] = "T"

    min_x = min([x for x, _ in graph])
    max_x = max([x for x, _ in graph])
    min_y = min([y for _, y in graph])
    max_y = max([y for _, y in graph])
    print(min_x, max_x, min_y, max_y)
    display = []
    for y in range(min_y, max_y + 1):
        display.append([])
        for x in range(min_x, max_x + 1):
            display[y].append(graph[(x, y)] if (x, y) in graph else ".")
    for r in display:
        print("".join(r))


def handle_part_1(lines: list[str]) -> int:
    graph = {}
    seed = int(lines[0])
    target: tuple[int, int] = tuple(map(int, lines[1].split(" ")))
    start = (1, 1)

    return bfs(start, target, seed)


def handle_part_2(lines: list[str]) -> int:
    graph = {}
    seed = int(lines[0])
    start = (1, 1)

    steps = 0
    to_visit = [(start, steps)]
    visited = set()

    while steps <= 50:
        current, steps = to_visit.pop(0)

        if current in visited:
            continue

        for n in get_neighbors(current, seed):
            to_visit.append((n, steps + 1))
        visited.add(current)

    return len(visited) - 1  # the last one in the visited is 51 steps ahead
