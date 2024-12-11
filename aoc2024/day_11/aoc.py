from time import time
from typing import Counter

# memoization
counts = {}


def get_stones_count(stone, nb):
    if nb == 0:
        return 1

    if (stone, nb) in counts:
        return counts[(stone, nb)]

    count = 0
    s_stone = str(stone)
    l_stone = len(s_stone)

    if stone == 0:
        count = get_stones_count(1, nb - 1)
    elif l_stone % 2 == 0:
        count = get_stones_count(
            int(s_stone[: l_stone // 2]), nb - 1
        ) + get_stones_count(int(s_stone[l_stone // 2 :]), nb - 1)

    else:
        count = get_stones_count(stone * 2024, nb - 1)

    counts[(stone, nb)] = count
    return count


def blink(stones: dict[int, int]) -> dict[int, int]:
    new_stones = {}

    def add(s, n):
        if s not in new_stones:
            new_stones[s] = 0
        new_stones[s] += nb

    for stone, nb in stones.items():
        if stone == 0:
            add(1, nb)
            continue

        s_stone = str(stone)
        l_stone = len(s_stone)
        if l_stone % 2 != 0:
            add(stone * 2024, nb)
            continue

        left = int(s_stone[: l_stone // 2])
        right = int(s_stone[l_stone // 2 :])
        add(left, nb)
        add(right, nb)
    return new_stones


def handle_part_1(lines: list[str]) -> int:
    start = time()
    stones = dict(Counter(list(map(int, lines[0].split()))))
    for _ in range(25):
        stones = blink(stones)
    print(
        f"Part 1 (25 blinks) with a Counter Map : {sum(x for x in stones.values())} in  {time()-start}s"
    )

    start = time()
    stones = list(map(int, lines[0].split()))
    print(
        f"Part 1 (25 blinks) with a recursive function : {sum(get_stones_count(x, 25) for x in stones)} {time()-start}s"
    )
    return sum(get_stones_count(x, 25) for x in stones)


def handle_part_2(lines: list[str]) -> int:
    start = time()
    stones = dict(Counter(list(map(int, lines[0].split()))))
    for _ in range(75):
        stones = blink(stones)
    print(
        f"Part 1 (75 blinks) with a Counter Map : {sum(x for x in stones.values())} in  {time()-start}s"
    )

    start = time()
    stones = list(map(int, lines[0].split()))
    print(
        f"Part 1 (75 blinks) with a recursive function : {sum(get_stones_count(x, 75) for x in stones)} {time()-start}s"
    )
    return sum(get_stones_count(x, 75) for x in stones)
