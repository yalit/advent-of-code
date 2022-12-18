# each rock is represented like
# {
# 'h': X, # height of rock
# 'w': Y, # width of rock
# 'f': [(X, Y), ...] # which place is filled on top row (compared to bottom left)
# }
rocks = [
    {
        'h': 1,
        'w': 4,
        'f': [(0, 0), (1, 0), (2, 0), (3, 0)]
    },
    {
        'h': 3,
        'w': 3,
        'f': [(1, 0), (1, 1), (1, 2), (0, 1), (2, 1)]
    },
    {
        'h': 3,
        'w': 3,
        'f': [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    },
    {
        'h': 4,
        'w': 1,
        'f': [(0, 0), (0, 1), (0, 2), (0, 3)]
    },
    {
        'h': 2,
        'w': 2,
        'f': [(0, 0), (0, 1), (1, 0), (1, 1)]
    }
]


def canBeHere(x, y, rock, existing):
    for x in [(x + rx, y + ry) for rx, ry in rock['f']]:
        if x in existing:
            return False
    return True


def simulateRocksFalling(moves, length):
    maxH = 0
    rested = False
    m = 0
    rockType = 0
    existingRocks = set([(x, 0) for x in range(7)])
    nbRockRested = 0
    while nbRockRested < length:
        fallingRock = [2, maxH + 4]
        rested = False  # start position of bottom left corner of new rock

        while not rested and nbRockRested < length:
            # 1 : move if possible
            newX = fallingRock[0] + 1 if moves[m] == ">" else fallingRock[0] - 1
            if 0 <= newX and newX + rocks[rockType]['w'] <= 7 and canBeHere(newX, fallingRock[1], rocks[rockType],
                                                                            existingRocks):
                fallingRock[0] = newX
            m = (m + 1) % len(moves)

            # 2 : move downwards if possible
            newY = fallingRock[1] - 1
            if not canBeHere(fallingRock[0], newY, rocks[rockType], existingRocks):
                rested = True
                maxH = max(maxH, fallingRock[1] - 1 + rocks[rockType]['h'])
                for x in [(fallingRock[0] + rx, fallingRock[1] + ry) for rx, ry in rocks[rockType]['f']]:
                    existingRocks.add(x)

                nbRockRested += 1
                rockType = (rockType + 1) % len(rocks)
                continue

            fallingRock[1] = newY

    return maxH, existingRocks


def handle_part_1(lines: list[str]) -> int:
    moves = lines[0]
    return simulateRocksFalling(moves, 2022)[0]


def handle_part_2(lines: list[str]) -> int:
    moves = lines[0]
    maxH, existingRocks,  = simulateRocksFalling(moves, 2022)

    t = {}
    for x, y in existingRocks:
        if y not in t:
            t[y] = []
        t[y].append(x)

    pile = [t[x] for x in sorted(t)]
    existPattern = False
    start, end = 0, 1
    while not existPattern and start < len(pile):
        end = 1
        while not existPattern and end < len(pile):
            p1 = pile[start:end]
            p2 = pile[start + end:start + end + end]
            existPattern = p1 == p2 and (start - end) % len(moves) == 0
            end += 1
        start += 1

    start -= 1
    end -= 1
    print(existPattern, start, end)
    return maxH
