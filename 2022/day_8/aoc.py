from libraries.array import transpose


def handle_part_1(lines: list[str]) -> int:
    columns = transpose(lines)
    nbVisible = (len(lines) + len(columns)) * 2 - 4

    for x in range(1, len(lines) - 1):
        for y in range(1, len(columns) - 1):
            if lines[x][y] > max(lines[x][0:y]) or lines[x][y] > max(lines[x][y+1:]) or columns[y][x] > max(columns[y][0:x]) or columns[y][x] > max(columns[y][x+1:]):
                nbVisible += 1

    return nbVisible


def handle_part_2(lines: list[str]) -> int:
    lines = [[int(x) for x in l] for l in lines]
    columns = transpose(lines)
    highestScenicScore = 0

    def getScenicScore(v: str, east: list[str], south: list[str], west: list[str], north: list[str]) -> int:
        def dirScenicScore(value: str, d: list[str]) -> int:
            higher = [1 if x >= value else 0 for x in d]
            return len(d) if 1 not in higher else higher.index(1) + 1

        return dirScenicScore(v, east) * dirScenicScore(v, south) * dirScenicScore(v, west) * dirScenicScore(v, north)

    for x in range(1, len(lines) - 1):
        for y in range(1, len(columns) - 1):
            scenicScore = getScenicScore(lines[x][y], lines[x][y+1:], columns[y][x+1:], list(reversed(lines[x][0:y])), list(reversed(columns[y][0:x])))
            highestScenicScore = scenicScore if scenicScore > highestScenicScore else highestScenicScore

    return highestScenicScore
