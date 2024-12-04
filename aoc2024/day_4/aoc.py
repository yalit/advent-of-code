from python.libraries.utils import named_directions as directions

possible_mas = [
    ((1, 1, "A"), (2, 0, "S"), (0, 2, "M"), (2, 2, "S")),
    ((1, -1, "A"), (0, -2, "S"), (2, 0, "M"), (2, -2, "S")),
    ((-1, -1, "A"), (-2, 0, "S"), (0, -2, "M"), (-2, -2, "S")),
    ((-1, 1, "A"), (0, 2, "S"), (-2, 0, "M"), (-2, 2, "S")),
]


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
    board = {(x, y): c for y, row in enumerate(lines) for x, c in enumerate(row)}
    exes = set(pos for pos in board if board[pos] == "X")

    total = 0
    for pos in exes:
        for dir in directions:
            total += 1 if is_xmas(board, pos, dir) else 0
    return total


def handle_part_2(lines: list[str]) -> int:
    board = {(x, y): c for y, row in enumerate(lines) for x, c in enumerate(row)}
    mms = set(pos for pos in board if board[pos] == "M")

    total = 0
    for pos in mms:
        x, y = pos
        for poss in possible_mas:
            total += (
                1
                if all(
                    (x + dx, y + dy) in board and board[(x + dx, y + dy)] == letter
                    for dx, dy, letter in poss
                )
                else 0
            )
    return total
