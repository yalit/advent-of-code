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


def handle_part_1(lines: list[str]) -> int:
    stones = list(map(int, lines[0].split()))
    return sum(get_stones_count(x, 25) for x in stones)


def handle_part_2(lines: list[str]) -> int:
    stones = list(map(int, lines[0].split()))
    return sum(get_stones_count(x, 75) for x in stones)
