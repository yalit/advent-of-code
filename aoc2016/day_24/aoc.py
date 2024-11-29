def bfs(map, start, nodes):
    to_visit = [(start, 0)]
    visited = set()
    distances = {}

    while to_visit:
        current, steps = to_visit.pop(0)

        if map[current] in nodes:
            distances[map[current]] = steps

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            n = (current[0] + dx, current[1] + dy)
            if n not in map:
                continue

            if n in visited:
                continue

            if (n, steps + 1) in to_visit:
                continue

            to_visit.append((n, steps + 1))
        visited.add(current)

    return distances


def handle_part_1(lines: list[str]) -> int:
    map = {}
    nodes = {}
    distances = {}

    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == "#":
                continue
            map[(r, c)] = char
            if char != ".":
                nodes[char] = (r, c)

    for n in nodes:
        distances[n] = bfs(map, nodes[n], nodes)

    start = "0"
    to_check = [([start], 0)]

    min_cost = 1000000000

    while to_check:
        path, cost = to_check.pop(0)

        if len(path) == len(nodes):
            min_cost = min(cost, min_cost)
            continue

        for n in distances[path[-1]]:
            if n in path:
                continue

            to_check.append((path + [n], cost + distances[path[-1]][n]))

    return min_cost


def handle_part_2(lines: list[str]) -> int:
    map = {}
    nodes = {}
    distances = {}

    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == "#":
                continue
            map[(r, c)] = char
            if char != ".":
                nodes[char] = (r, c)

    for n in nodes:
        distances[n] = bfs(map, nodes[n], nodes)

    start = "0"
    to_check = [([start], 0)]

    min_cost = 10000000000000
    while to_check:
        path, cost = to_check.pop(0)

        if len(path) == len(nodes) + 1:
            min_cost = min(cost, min_cost)
            continue

        if len(path) == len(nodes):
            to_check.append((path + ["0"], cost + distances[path[-1]]["0"]))

        else:
            for n in distances[path[-1]]:
                if n in path:
                    continue

                to_check.append((path + [n], cost + distances[path[-1]][n]))

    return min_cost
