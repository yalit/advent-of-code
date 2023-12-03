import re

from python.libraries.utils import neighbors
from python.libraries.array import inbound


def handle_part_1(lines: list[str]) -> int:
    s = 0
    m = [list(l) for l in lines]
    sns = {}
    h = len(m)
    w = len(m[0])

    for r, row in enumerate(lines):
        ns = re.finditer(r'(\d+)', row)
        for n in ns:
            for c in range(n.start(), n.end()):
                sns[(r, c)] = int(n.group())

    for r, row in enumerate(m):
        for c, char in enumerate(row):
            if char.isdigit() or char == '.':
                continue
            gs = set()
            for [dr, dc] in neighbors:
                if inbound(r+dr, c+dc, h, w) and lines[r+dr][c+dc].isdigit():
                    gs.add(sns[(r+dr,c+dc)])
            for n in gs:
                s += n
    return s


def handle_part_2(lines: list[str]) -> int:
    s = 0
    m = [list(l) for l in lines]
    sns = {}
    h = len(m)
    w = len(m[0])

    for r, row in enumerate(lines):
        ns = re.finditer(r'(\d+)', row)
        for n in ns:
            for c in range(n.start(), n.end()):
                sns[(r, c)] = int(n.group())

    for r, row in enumerate(lines):
        gears = re.finditer(r'(\*)', row)
        for gear in gears:
            gear_set = set()
            for [dr, dc] in neighbors:
                c = gear.start()
                if inbound(r + dr, c + dc, h, w) and (r + dr, c + dc) in sns:
                    gear_set.add(sns[(r + dr, c + dc)])
            if len(gear_set) == 2:
                s += list(gear_set)[0] * list(gear_set)[1]

    return s
