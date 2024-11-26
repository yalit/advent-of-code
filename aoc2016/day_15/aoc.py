import re


def isTime(t, discs):
    return all((t + d[0] - (d[1] - d[2])) % d[1] == 0 for d in discs)


def handle_part_1(lines: list[str]) -> int:
    discs = []
    for line in lines:
        g = re.match(
            r"Disc #(\d) has (\d+) positions; at time=0, it is at position (\d+).", line
        )
        if g is None:
            continue
        discs.append((int(g.groups()[0]), int(g.groups()[1]), int(g.groups()[2])))

    timer = 0

    while not isTime(timer, discs):
        timer += 1
    return timer


def handle_part_2(lines: list[str]) -> int:
    discs = []
    for line in lines:
        g = re.match(
            r"Disc #(\d) has (\d+) positions; at time=0, it is at position (\d+).", line
        )
        if g is None:
            continue
        discs.append((int(g.groups()[0]), int(g.groups()[1]), int(g.groups()[2])))

    discs.append((len(discs) + 1, 11, 0))
    timer = 0

    while not isTime(timer, discs):
        timer += 1
    return timer
