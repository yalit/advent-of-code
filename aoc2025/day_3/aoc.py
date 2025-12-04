def handle_part_1(lines: list[str]) -> int:
    input = [list(map(int, line)) for line in lines]

    total = 0
    for bank in input:
        a = max(bank[:-1])
        b = max(bank[bank.index(a) + 1:])
        total += int(f"{a}{b}")
    return total


def handle_part_2(lines: list[str]) -> int:
    input = [list(map(int, line)) for line in lines]

    total = 0
    for bank in input:
        jolt = ""
        idx = 0
        for i in range(12):
            last = -1 * (11 - i) if i < 11 else len(bank)
            n = max(bank[idx:last])
            jolt += str(n)
            idx = bank[idx:].index(n)+idx+1

        total += int(jolt)
    return total
