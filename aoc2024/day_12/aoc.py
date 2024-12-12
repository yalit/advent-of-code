from collections import deque


def get_plot_data(
    grid: list[list[str]], grid_set: set[tuple[int, int]], pos: tuple[int, int]
) -> tuple[set[tuple[int, int]], int, dict[tuple[int, int], set[tuple[int, int]]]]:
    plot = {pos}
    pr, pc = pos

    to_visit = deque([pos])
    area = 0
    neighbors = {}
    while to_visit:
        r, c = to_visit.popleft()

        neighbors[(r, c)] = set()
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (nr, nc) not in grid_set:
                continue
            if grid[nr][nc] != grid[pr][pc]:
                continue
            neighbors[(r, c)].add((nr, nc))

            if (nr, nc) in plot:
                continue
            to_visit.append((nr, nc))
            plot.add((nr, nc))

        area += 4 - len(neighbors[(r, c)])

    return plot, area, neighbors


def get_sides(plot, neighbors):
    neighbors_on_side = [pos for pos in neighbors if len(neighbors) > 0]

    sides = set()
    for pos in neighbors_on_side:
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if (pos[0] + dr, pos[1] + dc) not in plot:
                sides.add((pos, dr, dc))

    nb_sides = 0
    while sides:
        to_check = [sides.pop()]

        while to_check:
            pos, dr, dc = to_check.pop()

            for nr, nc in neighbors[pos]:
                if (((nr, nc), dr, dc)) in sides:
                    to_check.append(((nr, nc), dr, dc))
                    sides.remove(((nr, nc), dr, dc))
        nb_sides += 1

    return nb_sides


def handle_part_1(lines: list[str]) -> int:
    grid = [[a for a in line] for line in lines]
    grid_set = set()

    for r, line in enumerate(lines):
        for c, _ in enumerate(line):
            grid_set.add((r, c))

    price = 0
    while grid_set:
        pos = grid_set.pop()
        grid_set.add(pos)

        plot, area, _ = get_plot_data(grid, grid_set, pos)
        price += len(plot) * area
        grid_set -= plot

    return price


def handle_part_2(lines: list[str]) -> int:
    grid = [[a for a in line] for line in lines]
    grid_set = set()

    for r, line in enumerate(lines):
        for c, _ in enumerate(line):
            grid_set.add((r, c))

    price = 0
    while grid_set:
        pos = grid_set.pop()
        grid_set.add(pos)

        plot, area, neighbors = get_plot_data(grid, grid_set, pos)
        sides = get_sides(plot, neighbors)
        price += len(plot) * sides
        grid_set -= plot

    return price
