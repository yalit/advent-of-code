import sys

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def next_position(position: tuple[int, int], direction: str) -> tuple[int, int]:
    return (
        position[0] + directions[direction][0],
        position[1] + directions[direction][1],
    )


def handle_part_1(lines: list[str]) -> int:
    pos = (0, 0)
    walls = set()
    boxes = set()
    moves = lines[-1]

    for r, line in enumerate(lines):
        if line == "":
            break
        for c, element in enumerate(line):
            if element == "#":
                walls.add((r, c))
            if element == "O":
                boxes.add((r, c))
            if element == "@":
                pos = (r, c)

    def movable(
        position: tuple[int, int], direction: str, movables: list[tuple[int, int]]
    ) -> list[tuple[int, int]]:
        next_pos = next_position(position, direction)

        if next_pos in walls:
            return []

        if next_pos not in boxes:
            return movables + [position]

        return movable(next_pos, direction, movables + [position])

    for dir in moves:
        movables = movable(pos, dir, [])
        if not movables:
            continue

        # remove the current movable boxes positions
        boxes = boxes - set(movables[1:])
        # add the new positions
        for box in movables[1:]:
            boxes.add(next_position(box, dir))
        # the first movable element is the current position
        pos = next_position(movables[0], dir)

    return sum(100 * r + c for r, c in boxes)


def handle_part_2(lines: list[str]) -> int:
    pr, pc = (0, 0)
    walls = set()
    boxes = set()
    empty = set()
    moves = lines[-1]

    for r, line in enumerate(lines):
        if line == "":
            break
        for c, element in enumerate(line):
            if element == "#":
                walls.add((r, 2 * c))
                walls.add((r, (2 * c) + 1))
            if element == "O":
                boxes.add((r, 2 * c))
            if element == "@":
                pr, pc = (r, 2 * c)
                empty.add((r, (c * 2)+1))
            if element == ".":
                empty.add((r, c * 2))
                empty.add((r, (c * 2)+1))

    def visualize(dir, replace=True):
        if replace:
            for _ in range(len(lines) - 1):
                sys.stdout.write("\033[F")

        print(f"Moving in direction {dir}")
        grid = [[" " for _ in range(len(lines[0]) * 2)] for _ in range(len(lines) - 2)]
        for r, c in walls:
            grid[r][c] = "#"

        for r, c in boxes:
            grid[r][c] = "["
            grid[r][c + 1] = "]"

        for r, c in empty:
            grid[r][c] = "."

        grid[pr][pc] = dir
        for row in grid:
            print("".join(row))

    visualize("",False)
    for dir in moves:
        nr, nc = next_position((pr, pc), dir)
        # if next is wall then no move...
        if (nr, nc) in walls:
            visualize(dir)
            continue
        # if next is empty then move directly
        if (nr, nc) in empty:
            empty.remove((nr, nc))
            empty.add((pr, pc))
            pr, pc = nr, nc
            visualize(dir)
            continue

        # if next is a box somehow...
        if dir == ">":
            nboxes = [(nr, nc)]
            nr, nc = nr, nc + 2
            while (nr, nc) in boxes:
                nboxes.append((nr, nc))
                nr, nc = nr, nc + 2

            # move only if the element after the boxes is empty
            if (nr, nc) in empty:
                empty.remove((nr, nc))
                empty.add((pr, pc))
                pr, pc = pr, pc + 1
                for br, bc in nboxes:
                    boxes.remove((br, bc))
                    boxes.add((br, bc + 1))

        if dir == "<":
            nboxes = []
            nr, nc = pr, pc - 2
            while (nr, nc) in boxes:
                nboxes.append((nr, nc))
                nr, nc = nr, nc - 2

            # move only if the element just before the boxes is empty
            if (nr, nc + 1) in empty:
                empty.remove((nr, nc + 1))
                empty.add((pr, pc))
                pr, pc = pr, pc - 1
                for br, bc in nboxes:
                    boxes.remove((br, bc))
                    boxes.add((br, bc - 1))

        if dir == "^":
            # each element in the nboxes list is all the box that will move for the the i+1 (i starting at 0) level after the current row
            nboxes = []
            # only start of boxes are stored in boxes so check the start and the end...
            if (nr, nc) in boxes:
                nboxes.append([(nr, nc)])
            else:
                nboxes.append([(nr, nc - 1)])

            # looking if all the elements above the to be moved boxes are empty or not...
            can_move = True
            while can_move:
                can_move = all(
                    (br - 1, bc) not in walls
                    and (br - 1, bc + 1) not in walls
                    for br, bc in nboxes[-1])
                if not can_move:
                    break
                next_level = set()
                for br, bc in nboxes[-1]:
                    if (br - 1, bc - 1) in boxes:
                        next_level.add((br - 1, bc - 1))
                    if (br - 1, bc) in boxes:
                        next_level.add((br - 1, bc))
                    if (br - 1, bc + 1) in boxes:
                        next_level.add((br - 1, bc + 1))
                if len(next_level) == 0:
                    break
                nboxes.append(list(next_level))
            if not can_move:
                visualize(dir)
                continue

            # each level is the list of the position of the start of the boxes that will move
            for level in reversed(nboxes):
                for br, bc in level:
                    if (br-1,bc) in empty:
                        empty.remove((br - 1, bc))
                    if (br-1,bc+1) in empty:
                        empty.remove((br - 1, bc + 1))
                    empty.add((br, bc))
                    empty.add((br, bc + 1))
                    boxes.remove((br,bc))
                    boxes.add((br-1,bc))
            empty.remove((pr - 1, pc))
            empty.add((pr, pc))
            pr, pc = pr - 1, pc

        if dir == "v":
            # each element in the nboxes list is all the box that will move for the i+1 (i starting at 0) level after the current row
            nboxes = []
            # only start of boxes are stored in boxes so check the start and the end...
            if (nr, nc) in boxes:
                nboxes.append([(nr, nc)])
            else:
                nboxes.append([(nr, nc - 1)])

            # looking if all the elements above the to be moved boxes are empty or not...
            can_move = True
            while can_move:
                can_move = all(
                    (br + 1, bc) not in walls
                    and (br + 1, bc + 1) not in walls
                    for br, bc in nboxes[-1])
                if not can_move:
                    break
                next_level = set()
                for br, bc in nboxes[-1]:
                    if (br + 1, bc - 1) in boxes:
                        next_level.add((br + 1, bc - 1))
                    if (br + 1, bc) in boxes:
                        next_level.add((br + 1, bc))
                    if (br + 1, bc + 1) in boxes:
                        next_level.add((br + 1, bc + 1))
                if len(next_level) == 0:
                    break
                nboxes.append(list(next_level))
            if not can_move:
                visualize(dir)
                continue

            # each level is the list of the position of the start of the boxes that will move
            for level in reversed(nboxes):
                for br, bc in level:
                    if (br + 1, bc) in empty:
                        empty.remove((br + 1, bc))
                    if (br + 1, bc + 1) in empty:
                        empty.remove((br + 1, bc + 1))
                    empty.add((br, bc))
                    empty.add((br, bc + 1))
                    boxes.remove((br,bc))
                    boxes.add((br+1,bc))
            empty.remove((pr + 1, pc))
            empty.add((pr, pc))
            pr, pc = pr + 1, pc

        visualize(dir)

    return sum(100 * r + c for r, c in boxes)
