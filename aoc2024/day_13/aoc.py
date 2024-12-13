import math
import re


def min_cost(lines: list[str], part2: bool) -> int:
    ax, ay = list(
        map(int, re.match(r"Button .: X\+(\d+), Y\+(\d+)", lines[0]).groups())
    )
    bx, by = list(
        map(int, re.match(r"Button .: X\+(\d+), Y\+(\d+)", lines[1]).groups())
    )
    tx, ty = list(map(int, re.match(r"Prize: X=(\d+), Y=(\d+)", lines[2]).groups()))

    if part2:
        tx, ty = tx + 10000000000000, ty + 10000000000000

    A = (tx * by - ty * bx) / (ax * by - ay * bx)
    B = (tx - ax * A) / bx
    if A > 0 and B > 0 and A == math.floor(A) and B == math.floor(B):
        return int(A) * 3 + int(B)

    return 0


def handle_part_1(lines: list[str]) -> int:
    nb_tokens = 0

    for i in range(0, len(lines), 4):
        nb_tokens += min_cost(lines[i : i + 4], False)

    return nb_tokens


def handle_part_2(lines: list[str]) -> int:
    nb_tokens = 0

    for i in range(0, len(lines), 4):
        nb_tokens += min_cost(lines[i : i + 4], True)

    return nb_tokens
