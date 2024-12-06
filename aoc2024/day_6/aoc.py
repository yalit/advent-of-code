# order based on (row,column) 0 = N and rotating clockwise


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def next_direction(direction):
    return (direction + 1) % len(directions)


def handle_part_1(lines: list[str]) -> int:
    w = len(lines[0])
    h = len(lines)

    start = (0, 0)
    for r, line in enumerate(lines):
        for c, element in enumerate(line):
            if element == "^":
                start = (r, c)

    positions = set([start])
    r, c = start
    dir = 0
    while True:
        n_r, n_c = r + directions[dir][0], c + directions[dir][1]

        if not (0 <= n_r < h and 0 <= n_c < w):
            break

        if lines[n_r][n_c] == "#":
            dir = next_direction(dir)
            continue

        r, c = n_r, n_c
        positions.add((r, c))

    return len(positions)


def handle_part_2(inp: list[str]) -> int:
    lines = [[x for x in row] for row in inp]
    w = len(lines[0])
    h = len(lines)

    start = (0, 0)
    for r, line in enumerate(lines):
        for c, element in enumerate(line):
            if element == "^":
                start = (r, c)
    dir = 0
    r, c = start

    def is_loop():
        path = set([(r, c, dir)])
        direction = dir
        row, column = start
        while True:
            n_row, n_column = (
                row + directions[direction][0],
                column + directions[direction][1],
            )

            # we go out... so no loop
            if not (0 <= n_row < h and 0 <= n_column < w):
                return False

            if lines[n_row][n_column] == "#":
                direction = next_direction(direction)
                continue

            # we find the same in the same direction... so loop
            if (n_row, n_column, direction) in path:
                return True

            row, column = n_row, n_column
            path.add((row, column, direction))

    total = 0
    for r, line in enumerate(lines):
        for c, element in enumerate(line):
            if element != ".":
                continue

            lines[r][c] = "#"
            total += 1 if is_loop() else 0
            lines[r][c] = "."

    return total
