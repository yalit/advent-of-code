from python.libraries.array import transpose

def handle_part_1(lines: list[str]) -> int:
    return get_min_dist(lines, 1)

def handle_part_2(lines: list[str]) -> int:
    return get_min_dist(lines, 1000000-1)

def get_min_dist(lines, additional):
    empty_rows = [r for r, row in enumerate(lines) if all([x == '.' for x in row])]
    empty_cols = [c for c, col in enumerate(transpose(lines)) if all([x == '.' for x in col])]
    galaxies = [(r,c) for r, row in enumerate(lines) for c, col in enumerate(row) if col == '#']

    total = 0
    for i, (r1, r2) in enumerate(galaxies):
        for (t1, t2) in galaxies[i + 1:]:
            total += abs(t1 - r1) + abs(t2 - r2)
            for r in empty_rows:
                if min(r1, t1) < r < max(r1, t1):
                    total += additional
            for c in empty_cols:
                if min(r2, t2) < c < max(r2, t2):
                    total += additional

    return total