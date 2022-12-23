from collections import Counter


def round(dirs, elves):
    proposals = {}
    for ex, ey in elves:
        if sum([1 if (ex + x, ey + y) in elves else 0 for x in range(-1, 2) for y in range(-1, 2) if
                not (x == 0 and y == 0)]) == 0:
            continue

        for dx, dy in dirs:
            if sum([1 if (ex + dx + (d if dx == 0 else 0), ey + dy + (d if dy == 0 else 0)) in elves else 0 for d in
                    range(-1, 2)]) == 0:
                proposals[(ex, ey)] = (ex + dx, ey + dy)
                break

    nb_proposals = Counter(proposals.values())
    moved = 0
    new_elves = set()
    for ex, ey in elves:
        if (ex, ey) in proposals and nb_proposals[proposals[(ex, ey)]] == 1:
            new_elves.add(proposals[(ex, ey)])
            moved += 1
        else:
            new_elves.add((ex, ey))

    return new_elves, moved


def handle_part_1(lines: list[str]) -> int:
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    elves = set([(x, y) for y, line in enumerate(lines) for x, e in enumerate(line) if e == '#'])

    for r in range(10):
        elves, _ = round(dirs, elves)
        dirs = [*dirs[1:], dirs[0]]

    minX, maxX, minY, maxY = (
        min([e[0] for e in elves]),
        max([e[0] for e in elves]),
        min([e[1] for e in elves]),
        max([e[1] for e in elves])
    )
    return (maxX - minX) * (maxY - minY) - len(elves)


def handle_part_2(lines: list[str]) -> int:
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    elves = set([(x, y) for y, line in enumerate(lines) for x, e in enumerate(line) if e == '#'])

    moved = len(elves)
    nb_round = 0
    while moved != 0:
        nb_round += 1
        elves, moved = round(dirs, elves)
        dirs = [*dirs[1:], dirs[0]]

    return nb_round
