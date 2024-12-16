import sys
from heapq import heappop, heappush
from typing import Any

from python.libraries.colors import ConsoleColors

dirs = [(-1,0), (0,1), (1,0), (0,-1)]

def distance(a: tuple[int,int], b: tuple[int,int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_nodes_and_endpoints(lines: list[str]) -> tuple[set[tuple[int,int]],tuple[int,int], tuple[int,int]]:
    start = (0,0)
    end = (0,0)
    nodes = set()

    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char != "#":
                nodes.add((r,c))
            if char == "S":
                start = (r,c)
            if char == "E":
                end = (r,c)

    return nodes, start, end

def get_min_cost(nodes: set[tuple[int,int]], start: tuple[int,int], end: tuple[int,int]) -> int|float:
    open = {(start, 1)}
    g_score = {n: float("inf") for n in nodes}
    g_score[start] = 0

    f_score = {n: float("inf") for n in nodes}
    f_score[start] = distance(start, end)
    came_from = {}

    while open:
        current, direction = sorted(open, key=lambda x: f_score[x[0]])[0]
        if current == end:
            return g_score[end]

        open.remove((current, direction))
        for d in [-1, 0, 1]:
            new_dir = (direction + d) % 4
            neighbor = (current[0] + dirs[new_dir][0], current[1] + dirs[new_dir][1])
            if neighbor not in nodes:
                continue
            tentative_g_score = g_score[current] + 1 if d == 0 else g_score[current] + 1001
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + distance(neighbor, end)
                if (neighbor, new_dir) not in open:
                    open.add((neighbor, new_dir))

def handle_part_1(lines: list[str]) -> int|float:
    nodes, start, end = get_nodes_and_endpoints(lines)
    return get_min_cost(nodes, start, end)

def handle_part_2(lines: list[str]) -> int:
    nodes, start, end = get_nodes_and_endpoints(lines)
    min_cost = get_min_cost(nodes, start, end)

    def visualize(path):
        grid = [["#" for _ in range(len(lines[0]))] for _ in range(len(lines))]
        for node in nodes:
            grid[node[0]][node[1]] = "."
        for node,direct in path:
            grid[node[0]][node[1]] = ConsoleColors.colorize("O", ConsoleColors.OKGREEN)
        grid[start[0]][start[1]] = ConsoleColors.colorize("S", ConsoleColors.OKCYAN)
        grid[end[0]][end[1]] = ConsoleColors.colorize("E", ConsoleColors.OKCYAN)
        for row in grid:
            print("".join(row))

    costs = {n: float("inf") for n in nodes}
    costs[start] = 0

    best_tiles = set()
    to_visit = [(0, start, 1, ())]
    coming_from = {n: set() for n in nodes}

    while to_visit:
        cost, current, direction, pathway = heappop(to_visit)

        if current == end:
            if cost == min_cost:
                for pos in pathway:
                    best_tiles.add(pos)
            continue

        for d in [-1,0,1]:
            new_dir = (direction + d) % 4
            neighbor = (current[0] + dirs[new_dir][0], current[1] + dirs[new_dir][1])
            if current == (8,15):
                pass
            if neighbor not in nodes:
                continue

            new_cost = cost + 1 if d == 0 else cost + 1001
            if new_cost <= costs[neighbor]+1000:
                coming_from[neighbor].add((current, new_dir))
                costs[neighbor] = new_cost
                heappush(to_visit, (new_cost, neighbor, new_dir, pathway + ((neighbor,new_dir),)))

    visualize(best_tiles)

    return len(set([pos for pos, _ in best_tiles])) + 1 # +1 for the start tile
