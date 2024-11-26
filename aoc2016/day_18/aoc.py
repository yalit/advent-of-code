def get_total_safe(map: str, h: int):
    w = len(map)
    total = map.count(".")

    for i in range(1, h):
        new_line = ""
        for c in range(w):
            previous = map[max(0, c - 1) : c + 2]
            if c == 0:
                previous = "." + previous
            if c == w - 1:
                previous = previous + "."

            new_line = new_line + (
                "^"
                if (previous.count("^") == 2 and previous[1] == "^")
                or (previous.count("^") == 1 and previous[1] == ".")
                else "."
            )
        map = new_line
        total += new_line.count(".")

    return total


def handle_part_1(lines: list[str]) -> int:
    return get_total_safe(lines[0], int(lines[1]))


def handle_part_2(lines: list[str]) -> int:
    return get_total_safe(lines[0], 10000 * int(lines[1]))
