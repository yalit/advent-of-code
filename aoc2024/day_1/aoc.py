from collections import Counter


def handle_part_1(lines: list[str]) -> int:
    r = [list(map(int, line.split("  "))) for line in lines]
    left = [a for a, _ in r]
    right = [a for _, a in r]

    return sum([abs(a - b) for a, b in zip(sorted(left), sorted(right))])


def handle_part_2(lines: list[str]) -> int:
    r = [list(map(int, line.split("  "))) for line in lines]
    left = [a for a, _ in r]
    right = Counter([a for _, a in r])

    return sum([a * right[a] for a in left])
