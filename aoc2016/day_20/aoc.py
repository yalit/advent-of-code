def handle_part_1(lines: list[str]) -> int:
    ranges = [(int(line.split("-")[0]), int(line.split("-")[1])) for line in lines]
    m = 0

    for min, max in sorted(ranges):
        if min > m:
            return m

        if max > m:
            m = max + 1
    return -1


def handle_part_2(lines: list[str]) -> int:
    ranges = [
        sorted((int(line.split("-")[0]), int(line.split("-")[1]))) for line in lines
    ]
    m = 0
    n = 0

    for min, ma in sorted(ranges):
        if min > m:
            n += min - m
        if ma > m:
            m = ma + 1

    return n
