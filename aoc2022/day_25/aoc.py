def snafuToInt(snafu) -> int:
    mapping = {'2': 2, '1': 1, '0': 0, '-': -1, "=": -2}
    return sum([(5 ** i) * mapping[x] for i, x in enumerate(reversed(snafu))])


def intToSnafu(n) -> str:
    mapping = {4: '-', 3: "="}
    if n <= 2:
        return str(n)
    if n % 5 <= 2:
        return intToSnafu(n // 5) + str(n % 5)
    return intToSnafu((n // 5) + 1) + mapping[n % 5]


def handle_part_1(lines: list[str]) -> str:
    return intToSnafu(sum([snafuToInt(line) for line in lines]))


def handle_part_2(lines: list[str]) -> str:
    return "Not part two needed... Thank you little elf..."
