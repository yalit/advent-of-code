import re


def nb_uncorrupted(line: str) -> list[tuple[int, int]]:
    uncorrupted = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
    muls = []
    for mul in uncorrupted:
        muls.append(
            list(map(int, re.match(r"mul\((\d{1,3}),(\d{1,3})\)", mul).groups()))
        )
    return muls


def handle_part_1(lines: list[str]) -> int:
    total = 0
    for line in lines:
        muls = nb_uncorrupted(line)
        total += sum(a * b for a, b in muls)
    return total


def handle_part_2(lines: list[str]) -> int:
    do_re = r"do\(\)"
    dont_re = r"don\'t\(\)"
    total = 0
    enabled = True
    for line in lines:
        c = 0
        for mul in re.finditer(r"mul\(\d{1,3},\d{1,3}\)", line):
            next = re.search(do_re if not enabled else dont_re, line[c:])
            if next is not None and mul.start() > next.start() + c:
                enabled = not enabled
                c = mul.start()

            if enabled:
                a, b = list(
                    map(
                        int,
                        re.match(r"mul\((\d{1,3}),(\d{1,3})\)", mul.group()).groups(),
                    )
                )
                total += a * b

    return total
