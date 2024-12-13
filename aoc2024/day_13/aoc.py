import re


def handle_part_1(lines: list[str]) -> int:
    nb_tokens = 0

    for i in range(0, len(lines), 4):
        ax, ay = list(
            map(int, re.match(r"Button .: X\+(\d+), Y\+(\d+)", lines[i]).groups())
        )
        bx, by = list(
            map(int, re.match(r"Button .: X\+(\d+), Y\+(\d+)", lines[i + 1]).groups())
        )
        tx, ty = list(
            map(int, re.match(r"Prize: X=(\d+), Y=(\d+)", lines[i + 2]).groups())
        )

        memoirs = {}

        def get_min_cost(na, nb):
            x = ax * na + bx * nb
            y = ay * na + by * nb
            if x == tx and y == ty:
                return na * 3 + nb

            if x > tx or y > ty:
                return float("inf")

            if (x, y) in memoirs:
                return memoirs[(x, y)]

            min_cost = min(
                get_min_cost(na + 1, nb),
                get_min_cost(na, nb + 1),
            )

            memoirs[(x, y)] = min_cost

            return min_cost

        min_tokens = get_min_cost(0, 0)
        if min_tokens < float("inf"):
            nb_tokens += min_tokens

    return nb_tokens


def handle_part_2(lines: list[str]) -> int:
    return 0
