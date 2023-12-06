import re
from functools import reduce


def handle_part_1(lines: list[str]) -> int:
    t = list(map(int, re.findall(r'(\d+)', lines[0])))
    d = list(map(int, re.findall(r'(\d+)', lines[1])))

    m = 1
    for i in range(len(t)):
        m *= len([(x, (t[i] - x) * x) for x in range(1, t[i]) if (t[i] - x) * x > d[i]])

    return m


def handle_part_2(lines: list[str]) -> int:
    t = int(lines[0].split(":")[1].replace(" ", ""))
    d = int(lines[1].split(":")[1].replace(" ", ""))

    m = 0
    for x in range(1, t):
        m += 1 if (t - x) * x > d else 0


    return m
