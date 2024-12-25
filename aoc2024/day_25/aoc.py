def fits(lock: list[int], key: list[int]) -> bool:
    return all(k <= 5 - lock[i]  for i, k in enumerate(key))

def handle_part_1(lines: list[str]) -> int:
    locks = []
    keys = []

    r = 0
    while r < len(lines):
        heights = [0 for _ in range(5)]
        isLock = all(c == '#' for c in lines[r])

        for i in range(1,6):
            line = lines[r+i]
            for c, element in enumerate(line):
                if element == '#':
                    heights[c] = heights[c] + 1
        if isLock:
            locks.append(heights)
        else:
            keys.append(heights)
        r += 8

    fit = 0
    for lock in locks:
        for key in keys:
            if fits(lock, key):
                print(f"{lock} -> {key}")
                fit += 1

    return fit


def handle_part_2(lines: list[str]) -> int:
    return 0
