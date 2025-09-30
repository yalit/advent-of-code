from typing import Iterator

digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

directNeighbors = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

diagNeighbors = [
    (1, 1),
    (1, -1),
    (-1, -1),
    (-1, 1),
]

neighbors = directNeighbors + diagNeighbors

named_directions: dict[str, tuple[int, int]] = {
    "N": (0, -1),
    "NE": (1, -1),
    "E": (1, 0),
    "SE": (1, 1),
    "S": (0, 1),
    "SW": (-1, 1),
    "W": (-1, 0),
    "NW": (-1, -1),
}

neighbors3d = [
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, -1),
    (0, -1, 0),
    (-1, 0, 0),
]

directions = {0: (0, 1), 90: (1, 0), 180: (0, -1), 270: (-1, 0)}
direction_changes = {
    0: {0: (0, 1), 90: (1, 0), 180: (0, -1), -90: (-1, 0)},
    90: {-90: (0, 1), 0: (1, 0), 90: (0, -1), 180: (-1, 0)},
    180: {180: (0, 1), -90: (1, 0), 0: (0, -1), 90: (-1, 0)},
    270: {90: (0, 1), 180: (1, 0), -90: (0, -1), 0: (-1, 0)},
}


# ranges = (min,max)[]
def merge_ranges(ranges):
    if len(ranges) == 0:
        return ranges

    ranges = sorted(ranges, key=lambda r: r[0])
    merged = [tuple(ranges[0])]
    idx = 0
    for r in ranges[1:]:
        if r[0] < merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], r[1]))
        else:
            merged.append(tuple(r))
    return merged


# r1 & r2 are tuple (start, end)
def intersect_range(r1, r2):
    if r1[0] > r2[1] or r1[1] < r2[0]:
        return None

    if r1[0] < r2[0]:
        return (r2[0], r1[1]) if r1[1] < r2[1] else r2

    return (r1[0], r2[1]) if r1[1] > r2[1] else r1


def lcm(*n):
    def _pgcd(a, b):
        while b:
            a, b = b, a % b
        return a

    p = abs(n[0] * n[1]) // _pgcd(n[0], n[1])
    for x in n[2:]:
        p = abs(p * x) // _pgcd(p, x)
    return p


def euclidian_distance(n1: tuple[int, int], n2: tuple[int, int]):
    return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])


def split_every_n(s: str, n: int) -> list[str]:
    """Split a string every n characters, using the specified delimiter."""
    return [s[i : i + n] for i in range(0, len(s), n)]