def get_grid(lines: list[str]) -> dict[tuple[int,int],str]:
    grid = {}

    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            if char != " ":
                grid[(r,c)] = char

    return grid

def get_next_pos_and_dir_and_diagram(grid, direction, pos, diagram):
    continue_dirs = {(0, 1): '-', (0, -1): '-', (1, 0): '|', (-1, 0): '|'}
    c = grid[pos]

    if c == "+":
        new_pos = pos
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = pos[0] + dr, pos[1] + dc
            if (nr, nc) in grid and grid[(nr, nc)] != continue_dirs[direction]:
                new_pos = (nr, nc)
                break
        if new_pos != pos:
            return new_pos, (new_pos[0] - pos[0], new_pos[1] - pos[1]), diagram
        else:
            return None, direction, diagram

    if c not in ['|', '-']:
        diagram += grid[pos]

    return (pos[0] + direction[0], pos[1] + direction[1]), direction, diagram

def handle_part_1(lines: list[str]) -> int:
    grid = get_grid(lines)
    direction = (1,0)
    diagram = ''
    pos = (0, lines[0].index('|'))

    while pos is not None and pos in grid:
        pos, direction, diagram = get_next_pos_and_dir_and_diagram(grid, direction, pos, diagram)

    return diagram


def handle_part_2(lines: list[str]) -> int:
    grid = get_grid(lines)
    direction = (1,0)
    diagram = ''
    pos = (0, lines[0].index('|'))
    nb_steps = 0

    while pos is not None and pos in grid:
        pos, direction, diagram = get_next_pos_and_dir_and_diagram(grid, direction, pos, diagram)
        nb_steps += 1

    return nb_steps
