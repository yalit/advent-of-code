from hashlib import md5
from typing import Generator

height, width = 4, 4


def neighbors(pos: tuple[int, int], path: str, seed: str):
    hash = md5((seed + path).encode("utf-8")).hexdigest()[:4]
    dirs = {"U": 0, "D": 1, "L": 2, "R": 3}
    for dx, dy, d in [(0, 1, "D"), (0, -1, "U"), (1, 0, "R"), (-1, 0, "L")]:
        x, y = pos[0] + dx, pos[1] + dy
        if not (0 <= x < width and 0 <= y < height):
            continue

        if hash[dirs[d]] in ["b", "c", "d", "e", "f"]:
            yield ((x, y), d)


def search_path(
    start: tuple[int, int], target: tuple[int, int], seed: str, longest: bool = False
) -> str:
    path = ""
    to_visit = [(start, path)]
    all_paths = []

    while to_visit:
        pos, path = to_visit.pop(0)

        if pos == target:
            if longest:
                all_paths.append(path)
                continue
            else:
                return path

        for n, d in neighbors(pos, path, seed):
            to_visit.append((n, path + d))

    return sorted(all_paths, key=len)[-1]


def handle_part_1(lines: list[str]) -> str:
    s, t = (0, 0), (3, 3)

    return search_path(s, t, lines[0])


def handle_part_2(lines: list[str]) -> int:
    s, t = (0, 0), (3, 3)

    return len(search_path(s, t, lines[0], True))
