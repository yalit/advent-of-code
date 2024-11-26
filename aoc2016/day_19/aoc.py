import collections


def handle_part_1(lines: list[str]) -> int:
    elves = [(x + 1, 1) for x in range(int(lines[0]))]
    nb = 0

    while elves[nb][1] != len(elves):
        e, p = elves[nb]

        next_nb = (nb + 1) % len(elves)
        while elves[next_nb][1] == 0:
            next_nb = (next_nb + 1) % len(elves)

        ne, np = elves[next_nb]

        if p != 0:
            elves[nb] = (e, p + np)
            elves[next_nb] = (ne, 0)
        nb = next_nb
    return elves[nb][0]


def handle_part_2(lines: list[str]) -> int:
    left = collections.deque()
    right = collections.deque()
    for i in range(1, int(lines[0]) + 1):
        if i < (int(lines[0]) // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0] or right[0]
