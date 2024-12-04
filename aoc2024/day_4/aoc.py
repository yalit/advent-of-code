directions = {
    "N": (0, -1),
    "NE": (1, -1),
    "E": (1, 0),
    "SE": (1, 1),
    "S": (0, 1),
    "SW": (-1, 1),
    "W": (-1, 0),
    "NW": (-1, -1),
}

opposites_direction = {"SE": "NE", "NE": "NW", "SW": "SE", "NW": "SW"}


def is_xmas(
    board: dict[tuple[int, int], str], pos: tuple[int, int], dir: str, target="XMAS"
):
    if pos not in board:
        return False
    xmas = board[pos]
    dx, dy = directions[dir]
    for i in range(1, len(target)):
        x, y = pos[0] + i * dx, pos[1] + i * dy
        if (x, y) not in board:
            return False
        xmas += board[(x, y)]
    return xmas == target


def handle_part_1(lines: list[str]) -> int:
    board = {}
    exes = set()
    for y, r in enumerate(lines):
        for x, c in enumerate(lines[y]):
            board[(x, y)] = c
            if c == "X":
                exes.add((x, y))

    total = 0
    for pos in exes:
        for dir in directions:
            total += 1 if is_xmas(board, pos, dir) else 0
    return total


def handle_part_2(lines: list[str]) -> int:
    board = {}
    mms = set()
    for y, r in enumerate(lines):
        for x, c in enumerate(lines[y]):
            board[(x, y)] = c
            if c == "M":
                mms.add((x, y))

    total = 0
    mass = set()
    for pos in mms:
        for dir in directions:
            if len(dir) == 1:
                continue
            if is_xmas(board, pos, dir, "MAS"):
                # storing the 'A' position
                mass.add(
                    ((pos[0] + directions[dir][0], pos[1] + directions[dir][1]), dir)
                )

    for mas in mass:
        pos, dir = mas
        for n_mas in mass:
            if mas == n_mas:
                continue

            n_pos, n_dir = n_mas

            if pos != n_pos:
                continue

            total += 1 if opposites_direction[dir] == n_dir else 0
    return total
