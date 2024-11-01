from python.libraries.array import visualize_grid_dict
from python.libraries.utils import directNeighbors, diagNeighbors


def get_grid(lines: list[str]) -> dict:
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    return grid

def find_keys_around(grid: dict, pos: tuple[int, int]) -> list[tuple[int, str, int, str]]:
    to_visit = [(pos, [], 0)]
    keys = []
    visited = set()

    while to_visit:
        current_pos, direct_connection, steps = to_visit.pop(0)
        visited.add(current_pos)

        connection = []

        if grid[current_pos].islower() and current_pos != pos:
            keys.append((current_pos, direct_connection, steps, grid[current_pos]))
            connection.append(grid[current_pos])
        if grid[current_pos].isupper():
            connection.append(grid[current_pos])
        x, y = current_pos
        to_visit.extend([((x+dx, y+dy), direct_connection[:] + connection, steps+1) for dx, dy in directNeighbors if (x+dx, y+dy) in grid and (x+dx,y+dy) not in visited and grid[(x+dx, y+dy)] != '#'])

    return keys


def handle_part_1(lines: list[str]) -> int:
    grid = get_grid(lines)
    start = next(k for k, v in grid.items() if v == '@')
    all_keys_with_position = tuple(sorted(tuple({(k, grid[k]) for k in grid if grid[k].islower()})))
    all_keys = tuple(sorted(tuple({v for k, v in all_keys_with_position})))
    print(all_keys)
    keys_around = {'@': find_keys_around(grid, start)}
    for pos, key in all_keys_with_position:
        keys_around[key] = find_keys_around(grid, pos)
    visualize_grid_dict(grid)

    scores_memoization = {}

    def score(pos, keys_found):
        if keys_found == all_keys:
            return 0

        if (pos, keys_found) in scores_memoization:
            return scores_memoization[(pos, keys_found)]

        scores = []

        temp_keys_around = [(p, s, k) for p, c, s, k in keys_around[grid[pos]] if k not in keys_found and all([d is None or d.lower() in keys_found for d in c])]

        for temp_position, steps, key in temp_keys_around:
            scores.append(score(temp_position, tuple(sorted(tuple(set(keys_found) | {key})))) + steps)

        s = min(scores) if scores else float('inf')
        scores_memoization[(pos, keys_found)] = s
        return s

    return score(start, ())


def handle_part_2(lines: list[str]) -> int:
    grid = get_grid(lines)
    start = next(k for k, v in grid.items() if v == '@')
    all_keys_with_position = tuple(sorted(tuple({(k, grid[k]) for k in grid if grid[k].islower()})))
    all_keys = tuple(sorted(tuple({v for k, v in all_keys_with_position})))
    print(all_keys)

    starts: list[tuple[int, int]] = [(start[0] + dx, start[1] + dy) for dx, dy in diagNeighbors]
    grid[start] = '#'
    for i,pos in enumerate(starts):
        x,y = pos
        grid[(x, y)] = str(i)
    for dx, dy in directNeighbors:
        grid[(start[0] + dx, start[1] + dy)] = '#'

    keys_around = {}
    for i, pos in enumerate(starts):
        keys_around[str(i)] = find_keys_around(grid, pos)

    for pos, key in all_keys_with_position:
        keys_around[key] = find_keys_around(grid, pos)

    visualize_grid_dict(grid)

    scores_memoization = {}

    def score(positions, keys_found, previous):
        if keys_found == all_keys:
            return 0

        if (positions, keys_found) in scores_memoization:
            return scores_memoization[(positions, keys_found)]

        scores = []

        for i, position in enumerate(positions):
            temp_keys_around = [(p, s, k) for p, c, s, k in keys_around[grid[position]] if k not in keys_found and all([d is None or d.lower() in keys_found for d in c])]
            for temp_position, steps, key in temp_keys_around:
                new_positions = list(positions)[:]
                new_positions[i] = temp_position
                scores.append(score(tuple(new_positions), tuple(sorted(tuple(set(keys_found) | {key}))), previous + [(grid[position], grid[temp_position], steps)]) + steps)


        s = min(scores) if scores else float('inf')
        scores_memoization[(positions, keys_found)] = s
        return s

    return score(tuple(starts), (), [])