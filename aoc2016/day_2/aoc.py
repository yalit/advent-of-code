dirs = {"U": (0, -1), "L": (-1, 0), "R": (1, 0), "D": (0, 1)}


def getCode(lines: list[str], keypad: dict[tuple[int, int], int | str]) -> str:
    position = (1, 1)  # 5

    code = []
    for line in lines:
        for c in line:
            tentative = (position[0] + dirs[c][0], position[1] + dirs[c][1])
            if tentative in keypad:
                position = tentative

        code.append(str(keypad[position]))

    return "".join(code)


def handle_part_1(lines: list[str]) -> str:
    keypad = {
        (0, 0): 1,
        (1, 0): 2,
        (2, 0): 3,
        (0, 1): 4,
        (1, 1): 5,
        (2, 1): 6,
        (0, 2): 7,
        (1, 2): 8,
        (2, 2): 9,
    }
    return getCode(lines, keypad)


def handle_part_2(lines: list[str]) -> str:
    keypad = {
        (2, 0): 1,
        (1, 1): 2,
        (2, 1): 3,
        (3, 1): 4,
        (0, 2): 5,
        (1, 2): 6,
        (2, 2): 7,
        (3, 2): 8,
        (4, 2): 9,
        (1, 3): "A",
        (2, 3): "B",
        (3, 3): "C",
        (2, 4): "D",
    }

    return getCode(lines, keypad)
