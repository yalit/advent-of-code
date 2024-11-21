import re
import functools
import string
from collections import Counter

alphabet = string.ascii_lowercase


def handle_part_1(lines: list[str]) -> int:
    rooms = [re.match(r"([a-z\-]+)(\d+)\[([a-z]+)\]", line).groups() for line in lines]

    ids: list[int] = []
    for room, sector, checksum in rooms:
        c = Counter(room.replace("-", ""))

        def keyCounter(a: str, b: str) -> int:
            if c[a] == c[b]:
                if a < b:
                    return -1
                elif a > b:
                    return 1
                else:
                    return 0
            return c[b] - c[a]

        k = "".join([x for x in sorted(c, key=functools.cmp_to_key(keyCounter))])
        if k[:5] == checksum:
            ids.append(int(sector))

    return sum(ids)


def handle_part_2(lines: list[str]) -> int:
    rooms = [re.match(r"([a-z\-]+)(\d+)\[([a-z]+)\]", line).groups() for line in lines]

    for room, sector, checksum in rooms:
        c = Counter(room.replace("-", ""))

        def keyCounter(a: str, b: str) -> int:
            if c[a] == c[b]:
                if a < b:
                    return -1
                elif a > b:
                    return 1
                else:
                    return 0
            return c[b] - c[a]

        k = "".join([x for x in sorted(c, key=functools.cmp_to_key(keyCounter))])
        if k[:5] != checksum:
            continue

        decypher = " ".join(
            [
                "".join(
                    [
                        alphabet[(alphabet.index(c) + 26 + (int(sector) % 26)) % 26]
                        for c in w
                    ]
                )
                for w in room.split("-")
            ]
        )
        if "north" in decypher:
            return int(sector)

    return -1
