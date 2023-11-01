import string
import sys
from itertools import chain

alphabet = string.ascii_lowercase


def findLeastPathFrom(s, e, nodes, w, h, min):
    visited = set()
    visited.add(s)

    toVisit = [s]
    steps = 0
    found = False
    while not found and steps < min:
        found = e in toVisit

        def neighbors(c):
            n = []
            for x in range(-1, 2):
                for y in range(-1, 2):
                    cx = c % w
                    cy = c // w
                    tx, ty, kn = cx + x, cy + y, (cy + y) * w + cx + x

                    if kn not in visited and not (tx == cx and ty == cy) and (tx == cx or ty == cy) and 0 <= tx < w and 0 <= ty < h and nodes[kn] - nodes[c] <= 1:
                        n.append(kn)
            return n

        def filterToVisit(n):
            if n in visited:
                return False
            visited.add(n)
            return True

        toVisit = list(filter(filterToVisit, chain(*[neighbors(x) for x in toVisit])))
        steps += 1 if not found else 0

    return steps if found else min


def handle_part_1(lines: list[str]) -> int:
    n = ''.join(lines)

    start, end = n.index('S'), n.index('E')
    n = n.replace('S', 'a')
    n = n.replace('E', 'z')
    n = [alphabet.index(a) for a in n]

    return findLeastPathFrom(start, end, n, len(lines[0]), len(lines), sys.maxsize)


def handle_part_2(lines: list[str]) -> int:
    n = ''.join(lines)

    end = n.index('E')
    n = n.replace('S', 'a')
    n = n.replace('E', 'z')
    n = [alphabet.index(a) for a in n]

    leastPath = sys.maxsize
    for k, a in enumerate(n):
        if a != 0:
            continue
        leastPath = findLeastPathFrom(k, end, n, len(lines[0]), len(lines), leastPath)

    return leastPath
