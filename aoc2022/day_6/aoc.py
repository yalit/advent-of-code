from collections import Counter


def get_marker(l: str, n: int):
    return [i + n for i in range(len(l) - n) if len(Counter(l[i:i + n])) == n][0]


def handle_part_1(lines: list[str]) -> int:
    return get_marker(lines[0], 4)


def handle_part_2(lines: list[str]) -> int:
    return get_marker(lines[0], 14)
