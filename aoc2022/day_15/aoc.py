import re
from functools import reduce


def manhattan(x, y):
    return abs(y[0]-x[0])+abs(y[1]-x[1])


def getRangesForY(d: set):
    deltas = set(d)
    sDeltas = sorted(deltas, key=lambda x: x[0])
    i = 0
    while i < len(sDeltas) - 1:
        # both are distinct
        if sDeltas[i][1] < sDeltas[i + 1][0] - 1:
            i += 1
            continue

        # merge as second start is lower of equal to end of previous
        deltas.remove(sDeltas[i])
        deltas.remove(sDeltas[i + 1])
        deltas.add((sDeltas[i][0],max(sDeltas[i][1], sDeltas[i+1][1])))
        sDeltas = sorted(deltas, key=lambda x: x[0])

    return deltas


def handle_part_1(lines: list[str]) -> int:
    sensors = []
    size = [0, 0]
    row = int(lines[0])

    for line in lines[2:]:
        sx, sy, bx, by = map(int, re.compile(r"-?\d+").findall(line))
        sensors.append(((sx, sy), manhattan((sx, sy), (bx, by))))
        size = [min(size[0], sx, bx), max(size[1], sx, bx)]

    deltas = set()
    for sensor in sensors:
        sX = sensor[0][0]
        sY = sensor[0][1]
        deltaX = sensor[1] - abs(sY - row)
        if deltaX < 0:
            continue
        deltas.add((sX - deltaX, sX + deltaX))

    deltas = getRangesForY(deltas)

    return reduce(lambda s, d: s + (d[1] - d[0]), deltas, 0)


def handle_part_2(lines: list[str]) -> int:
    sensors = []
    m = int(lines[1])
    deltas = {}
    lines = [map(int, re.compile(r"-?\d+").findall(line)) for line in lines[2:]]

    for sx, sy, bx, by in lines:
        dist = abs(sx-bx) + abs(sy-by)

        for row in range(m + 1):
            if row not in deltas:
                deltas[row] = set()
            deltaX = dist - abs(sy - row)
            if deltaX < 0:
                continue
            deltas[row].add((sx - deltaX if sx - deltaX >= 0 else 0, sx + deltaX if sx + deltaX <= m else m))

    signalRow = []
    for r in deltas:
        deltas[r] = sorted(getRangesForY(deltas[r]))
        if len(deltas[r]) > 1:
            signalRow.append(r)
            print(r, deltas[r])

    if len(signalRow) > 1:
        for r in signalRow:
            print(r, deltas[r])
        return -1

    r = signalRow[0]
    return ((deltas[r][0][1] + 1) * 4000000) + r
