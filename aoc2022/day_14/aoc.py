import functools
from functools import reduce

from libraries.array import visualize


def getReservoir(lines):
    heights = {}
    for line in lines:
        points = [list(map(int, point.split(','))) for point in line.split(' -> ')]
        lastPoint = points[0]
        if lastPoint[0] not in heights:
            heights[lastPoint[0]] = set()
        heights[lastPoint[0]].add(('🪨', lastPoint[1]))

        for currentPoint in points[1:]:
            for x in range(min(lastPoint[0], currentPoint[0]), max(lastPoint[0] + 1, currentPoint[0] + 1)):
                if x not in heights:
                    heights[x] = set()
                heights[x].add(('🪨', lastPoint[1]))

            for y in range(min(lastPoint[1], currentPoint[1]), max(lastPoint[1] + 1, currentPoint[1] + 1)):
                heights[lastPoint[0]].add(('🪨', y))
            lastPoint = currentPoint

    return heights, max([max([b[1] for b in heights[a]]) for a in heights])


def getNextBelow(s, h):
    sHeights = [a[1] for a in s]
    if h + 1 < max(sHeights) and h + 1 not in sHeights:
        return h + 1

    if h + 1 in sHeights:
        return h

    return -1


def getNextPositionOfSand(heights, x, y):
    if x not in heights:
        return -1, -1

    nextBelow = getNextBelow(heights[x], y)
    if nextBelow > y:
        return x, nextBelow

    for d in [-1, 1]:
        if x + d not in heights:
            return -1, -1
        nextBelow = getNextBelow(heights[x + d], y)
        if nextBelow == -1:
            return -1, -1
        if nextBelow > y:
            return x + d, y

    return x, y


def dropSand(heights, startX=500, startY=0, maxY=0):
    sx, sy = startX, startY
    nx, ny = sx, sy
    while True:
        nx, ny = getNextPositionOfSand(heights, nx, ny)
        if nx == -1:
            dropEnded = True
            break
        if nx == sx and ny == sy:
            heights[nx].add(('🍞', ny))
            break
        sx, sy = nx, ny

    return nx, ny


def displayMountain(heights):
    width = max(heights) - min(heights) + 3
    height = max([reduce(lambda h, x: h if x[1] <= h else x[1], heights[a], 0) for a in heights]) + 1
    m = min(heights)

    grid = [['⚪️' for _ in range(width)] for _ in range(height)]
    for x in heights:
        for y in heights[x]:
            grid[y[1]][x + 1 - m] = y[0]

    visualize(grid)


def handle_part_1(lines: list[str]) -> int:
    heights, _ = getReservoir(lines)

    displayMountain(heights)
    nbSand = 0
    while True:
        x, y = dropSand(heights)
        if x == -1:
            break

        nbSand += 1
        continue

    print('')
    print("####################")
    print('After sand drop')
    print("####################")
    print('')
    displayMountain(heights)
    return nbSand


def handle_part_2(lines: list[str]) -> int:
    heights, maxDepth = getReservoir(lines)

    for x in range(min(heights) - maxDepth, max(heights) + maxDepth):
        if x not in heights:
            heights[x] = set()
        heights[x].add(('🪨', maxDepth + 2))

    displayMountain(heights)
    nbSand = 0
    while True:
        x, y = dropSand(heights)
        if x == 500 and y == 0:
            break

        nbSand += 1
        continue

    print('')
    print("####################")
    print('After sand drop')
    print("####################")
    print('')
    displayMountain(heights)
    return nbSand + 1
