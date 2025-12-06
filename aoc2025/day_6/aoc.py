from functools import reduce

def handle_part_1(lines: list[str]) -> int:
    cols = [[int(line.split()[i]) for line in lines[:-1]] for i in range(len(lines[0].split()))]

    total = 0
    for i, t in enumerate(lines[-1].split()):
        if t == '+':
            total += sum(cols[i])
        if t == '*':
            total += reduce(lambda tot,x: tot*x, cols[i], 1)

    return total


def handle_part_2(lines: list[str]) -> int:
    total = 0

    numbers = []
    i = len(lines[0]) - 1
    while i >= 0:
        numbers.append(int("".join(line[i] for line in lines[:-1])))

        operator = lines[-1][i]
        if operator != " ":
            if operator == "+":
                total += sum(numbers)
            if operator == "*":
                total += reduce(lambda tot, x: tot * x, numbers, 1)
            numbers = []
            i -= 1

        i -= 1
    return total
