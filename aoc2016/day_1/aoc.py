dirs = {0: (0, -1), 90: (1, 0), 180: (0, 1), 270: (-1, 0)}


def handle_part_1(lines: list[str]) -> int:
    steps = map(lambda s: (s[0], int(s[1:])), lines[0].split(", "))

    dir = 0
    s = [0, 0]
    for rotation, distance in steps:
        angle = 90 if rotation == "R" else -90
        dir = (dir + 360 + angle) % 360
        s = [s[0] + dirs[dir][0] * distance, s[1] + dirs[dir][1] * distance]

    return abs(s[0]) + abs(s[1])


def handle_part_2(lines: list[str]) -> int:
    steps = map(lambda s: (s[0], int(s[1:])), lines[0].split(", "))

    dir = 0
    s = (0, 0)
    locations = {s}
    for rotation, distance in steps:
        angle = 90 if rotation == "R" else -90
        dir = (dir + 360 + angle) % 360
        for _ in range(distance):
            s = (s[0] + dirs[dir][0], s[1] + dirs[dir][1])
            if s in locations:
                return abs(s[0]) + abs(s[1])
            locations.add(s)

    return -1
