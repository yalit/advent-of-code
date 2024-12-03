import re


def nb_uncorrupted(line: str) -> list[tuple[int, int]]:
    uncorrupted = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
    muls = []
    for mul in uncorrupted:
        muls.append(list(map(int, mul[4:-1].split(","))))
    return muls


def handle_part_1(lines: list[str]) -> int:
    total = 0
    for line in lines:
        muls = nb_uncorrupted(line)
        total += sum(a * b for a, b in muls)
    return total


def handle_part_2(lines: list[str]) -> int:
    total = 0
    enabled = True
    for line in lines:
        for m in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", line):
            if m == "do()":
                enabled = True
            elif m == "don't()":
                enabled = False
            elif enabled:
                a, b = list(map(int, m[4:-1].split(",")))
                total += a * b

    return total
