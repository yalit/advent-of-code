# Coordinates [0,0], x=0, y=0
from functools import reduce

from libraries.array import visualize

movesHead = {
    'R': lambda c: [c[0] + 1, c[1]],
    'L': lambda c: [c[0] - 1, c[1]],
    'U': lambda c: [c[0], c[1] + 1],
    'D': lambda c: [c[0], c[1] - 1],
}

def whichMove(c1: list[int], c2: list[int]) -> str:
    if c2[0] == c1[0] or c1[1] == c2[1]:
        return 'line' if ((abs(c2[0] - c1[0]) if c2[0] > c1[0] else abs(c1[0] - c2[0])) > 1 or (abs(c2[1] - c1[1]) if c2[1] > c1[1] else abs(c1[1] - c2[1])) > 1) else 'no'

    return 'diag' if ((abs(c2[0] - c1[0]) if c2[0] > c1[0] else abs(c1[0] - c2[0])) + (abs(c2[1] - c1[1]) if c2[1] > c1[1] else abs(c1[1] - c2[1])) > 2) else 'no'


def moveKnot(prev: list, knot: list):
    mtx, mty = 0, 0
    if whichMove(knot, prev) == 'line':
        mtx = 1 if prev[0] > knot[0] + 1 else -1 if prev[0] < knot[0] - 1 else 0
        mty = 1 if prev[1] > knot[1] + 1 else -1 if prev[1] < knot[1] - 1 else 0
    elif whichMove(knot, prev) == 'diag':
        mtx = 1 if prev[0] > knot[0] else -1 if prev[0] < knot[0] else 0
        mty = 1 if prev[1] > knot[1] else -1 if prev[1] < knot[1] else 0
    return [knot[0] + mtx, knot[1] + mty]


def handleHeadMove(rope: list[list], direction: str):
    newPlacement = list(reversed([*rope]))
    for i in range(len(rope)):
        newPlacement[i] = movesHead[direction](newPlacement[i]) if i == 0 else moveKnot(newPlacement[i - 1], newPlacement[i])

    return list(reversed(newPlacement))


def handleRopeTravel(rope: list[list], moves: list[str], debug: bool = False) -> list[list]:
    visited = [rope[0]]
    for l in moves:
        for _ in range(int(l[2:])):
            rope = handleHeadMove(rope, l[0:1])
            if rope[0] not in visited:
                visited.append(rope[0])
    return visited


def handle_part_1(lines: list[str]) -> int:
    rope = [[0, 0] for _ in range(2)]
    return len(handleRopeTravel(rope, lines))


def handle_part_2(lines: list[str]) -> int:
    rope = [[0, 0] for _ in range(10)]
    return len(handleRopeTravel(rope, lines))
