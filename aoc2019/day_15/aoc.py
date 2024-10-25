from typing import Any, Dict, Tuple

from python.libraries.array import visualize, visualize_grid_dict
from python.libraries.intCode.InputRequestIntCodeComputer import InputRequestIntCodeComputer

backwards = {1: 2, 2: 1, 3: 4, 4: 3}
directions= {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}

def move(pos: Tuple[int, int], direction: int) -> Tuple[int, int]:
    return tuple(map(sum, zip(pos, directions[direction])))

def get_grid(start: Tuple[int, int], computer: InputRequestIntCodeComputer) -> Tuple[Dict[Tuple[int, int], str], Tuple[int, int]]:
    oxygen = None

    grid = {start: "S"}

    position = start
    remaining_for_next = {start: list(directions.keys())}
    path = []

    # while oxygen is not found
    while len(remaining_for_next) > 0:
        # get the next direction to go
        while position not in remaining_for_next:
            position, previous_dir = path.pop()
            computer.execute(backwards[previous_dir])

        direction = remaining_for_next[position].pop()
        if not remaining_for_next[position]:
            del remaining_for_next[position]
        status = computer.execute(direction)[-1]

        # if wall
        if status == 0:
            grid[move(position, direction)] = "#"
            continue

        # store into the path the position and how we exited that position
        path.append((position, direction))

        position = move(position, direction)

        if position not in grid:

            if status == 1:
                grid[position] = "."
            # if oxygen
            if status == 2:
                if oxygen is None:
                    oxygen = position
                grid[position] = "O"

            remaining_for_next[position] = list(directions.keys())

    return grid, oxygen

def handle_part_1(lines: list[str]) -> int:
    computer = InputRequestIntCodeComputer(list(map(int, lines[0].split(','))))
    start = (0, 0)
    grid, oxygen = get_grid(start, computer)

    print(f"Oxygen found at {oxygen}")
    to_visit = [(start, 0)]
    visited = set()

    while to_visit:
        position, steps = to_visit.pop()
        for direction in directions:
            new_position = move(position, direction)
            if new_position not in grid or grid[new_position] == "#" or new_position in visited:
                continue

            if grid[new_position] == "O":
                return steps + 1

            to_visit.append((new_position, steps + 1))
        visited.add(position)

    return None

def handle_part_2(lines: list[str]) -> int:
    computer = InputRequestIntCodeComputer(list(map(int, lines[0].split(','))))
    start = (0, 0)
    grid, oxygen = get_grid(start, computer)

    to_visit = [([oxygen], 0)]
    visited = set()
    minutes = 0

    print(f"Oxygen found at {oxygen}")
    visualize_grid_dict(grid)
    while to_visit:

        positions, steps = to_visit.pop()
        next_positions = []
        for position in positions:
            for direction in directions:
                new_position = move(position, direction)
                if new_position not in grid or grid[new_position] == "#" or new_position in visited:
                    continue

                next_positions.append(new_position)
                grid[new_position] = "O"

            visited.add(position)
        if len(next_positions) > 0:
            to_visit.append((next_positions, steps + 1))
        minutes = max(minutes, steps)

    return minutes