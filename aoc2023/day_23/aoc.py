from heapq import heappush, heappop
from python.libraries.utils import directNeighbors
from python.libraries.array import  inbound

hill_next = {
    '<': [(0, -1)],
    '>': [(0, 1)],
    '^': [(-1, 0)],
    'v': [(1, 0)],
    '.': directNeighbors
}

def handle_part_1(hill: list[str]) -> int:
    return find_longest_path(hill, True)


def handle_part_2(hill: list[str]) -> int:
    return find_longest_path(hill, False)

def find_longest_path(hill, steep):
    (start,) = [(0, c) for c, col in enumerate(hill[0]) if col != '#']
    (end,) = [(len(hill) - 1, c) for c, col in enumerate(hill[-1]) if col != '#']

    points = [start, end]

    for r,row in enumerate(hill):
        for c, col in enumerate(row):
            if col == '#':
                continue
            n = 0
            for dr, dc in directNeighbors:
                n_r, n_c = r + dr, c + dc
                if inbound(n_r, n_c, len(hill), len(hill[0])) and hill[n_r][n_c] != '#':
                    n +=1
            if n >= 3:
                points.append((r,c))

    relations = {k: {} for k in points}

    for r,c in points:
        to_visit = [((r,c), 0)]
        seen = {(r,c)}
        while to_visit:
            (tr, tc), path = to_visit.pop()

            if (tr, tc) in points and path != 0:
                relations[(r,c)][(tr,tc)] = path
                continue

            next_steps_delta = directNeighbors
            if steep:
                next_steps_delta = hill_next[hill[tr][tc]]

            for dr, dc in next_steps_delta:
                n_r, n_c = tr + dr, tc + dc
                if inbound(n_r, n_c, len(hill), len(hill[0])) and hill[n_r][n_c] != '#' and (n_r, n_c) not in seen:
                    to_visit.append(((n_r, n_c), path + 1))
            seen.add((tr, tc))

    return dfs(start, end, relations, set())

def dfs(step, target, graph, seen):
    if step == target:
        return 0

    m = -float("inf")

    seen.add(step)
    for nx in graph[step]:
        if nx not in seen:
            m = max(m, dfs(nx, target, graph, seen) + graph[step][nx])
    seen.remove(step)

    return m