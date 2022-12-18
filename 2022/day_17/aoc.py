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



def handle_part_1(lines: list[str]) -> int:
    moves = lines[0]
    maxH = 0
    rested = False
    m = 0
    rockType = 0
    existingRocks = set([(x, 0) for x in range(7)])
    nbRockRested = 0
    while nbRockRested < 2022:
        fallingRock = [2, maxH + 4]
        rested = False  # start position of bottom left corner of new rock

        while not rested and nbRockRested < 2022:
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

    return maxH


def handle_part_2(lines: list[str]) -> int:
    moves = lines[0]
    maxH = 0
    rested = False
    m = 0
    rockType = 0
    existingRocks = set([(x, 0) for x in range(7)])
    nbRockRested = 0

    increase = []
    heights = {}
    while nbRockRested < 2022:
        fallingRock = [2, maxH + 4]
        rested = False  # start position of bottom left corner of new rock

        while not rested and nbRockRested < 2022:
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
                prevH = maxH
                maxH = max(maxH, fallingRock[1] - 1 + rocks[rockType]['h'])
                increase.append(int(maxH - prevH))
                for x in [(fallingRock[0] + rx, fallingRock[1] + ry) for rx, ry in rocks[rockType]['f']]:
                    existingRocks.add(x)

                nbRockRested += 1
                heights[nbRockRested] = maxH
                rockType = (rockType + 1) % len(rocks)
                continue

            fallingRock[1] = newY

    start, end = 0, 1
    patternFound = False
    while not patternFound and start < len(increase):
        end = 1
        while not patternFound and start + end < len(increase) - start - end:
            left = increase[start:start+end]
            right = increase[start+end:start+end+end]
            patternFound = left == right and (start + end) % len(moves) == 0 and (start + end) % len(rocks) == 0
            end += 1
        start += 1

    print(patternFound, start, end, start + end, sum(left), sum(right), left, right)
    delta = 1000000000000 - start
    n = delta // len(left)
    h = n * sum(left) + heights[start+1] + sum(left[:(delta % len(left) % delta)-1])

    print(h)

    return maxH
