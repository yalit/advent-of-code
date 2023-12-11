import re
from python.libraries.array import transpose

def handle_part_1(lines: list[str]) -> int:
    return get_min_dist(lines, 1)


def handle_part_2(lines: list[str]) -> int:
    return get_min_dist(lines, 1000000-1)

def get_min_dist(lines, additional):
    galaxies = []

    empty_rows = []
    empty_cols = []
    for r, row in enumerate(lines):
        if all([x == '.' for x in row]):
            empty_rows.append(r)

    transposed = transpose(lines)
    for r, row in enumerate(transposed):
        if all([x == '.' for x in row]):
            empty_cols.append(r)

    for r, row in enumerate(lines):
        f = list(re.finditer("\#", row))
        for m in f:
            galaxies.append((r, m.start()))

    total = 0
    for i, g in enumerate(galaxies):
        for tg in galaxies[i + 1:]:
            min_dist = abs(tg[0] - g[0]) + abs(tg[1] - g[1])
            x = sorted((tg[0], g[0]))
            y = sorted((tg[1], g[1]))

            for r in empty_rows:
                if x[0] < r < x[1]:
                    min_dist += additional
            for c in empty_cols:
                if y[0] < c < y[1]:
                    min_dist += additional
            total += min_dist

    return total