def handle_part_1(lines: list[str]) -> int:
    w = len(lines[0])
    h = len(lines)

    antennas = {}

    for r, line in enumerate(lines):
        for c, point in enumerate(line):
            if point != ".":
                if point not in antennas:
                    antennas[point] = []
                antennas[point].append((r, c))

    antinodes = set()
    for frequency in antennas:
        for ra, ca in antennas[frequency]:
            for rb, cb in antennas[frequency]:
                if ra == rb and ca == cb:
                    continue

                dr = rb - ra
                dc = cb - ca
                # antinode on the "side of" a
                ara, aca = ra - dr, ca - dc
                if 0 <= ara < h and 0 <= aca < w:
                    antinodes.add((ara, aca))
                # antinode on the "side of" b
                arb, acb = rb + dr, cb + dc
                if 0 <= arb < h and 0 <= acb < w:
                    antinodes.add((arb, acb))

    return len(antinodes)


def handle_part_2(lines: list[str]) -> int:
    w = len(lines[0])
    h = len(lines)

    antennas = {}
    antinodes = set()

    for r, line in enumerate(lines):
        for c, point in enumerate(line):
            if point != ".":
                if point not in antennas:
                    antennas[point] = []
                antennas[point].append((r, c))
                antinodes.add((r, c))

    for frequency in antennas:
        for ra, ca in antennas[frequency]:
            for rb, cb in antennas[frequency]:
                if ra == rb and ca == cb:
                    continue

                dr = rb - ra
                dc = cb - ca
                # antinode on the "side of" a
                ara, aca = ra - dr, ca - dc
                while 0 <= ara < h and 0 <= aca < w:
                    antinodes.add((ara, aca))
                    ara, aca = ara - dr, aca - dc
                # antinode on the "side of" b
                arb, acb = rb + dr, cb + dc
                while 0 <= arb < h and 0 <= acb < w:
                    antinodes.add((arb, acb))
                    arb, acb = arb + dr, acb + dc

    return len(antinodes)
