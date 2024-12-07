def evaluate(numbers, join=False):
    operators = ["+", "*"]

    to_test = [(numbers[0], numbers[1:])]
    possibles = []
    while to_test:
        result, ns = to_test.pop()

        if len(ns) == 0:
            possibles.append(result)
            continue

        for op in operators:
            to_test.append((eval(f"{result}{op}{ns[0]}"), ns[1:]))

        if join:
            to_test.append((int(str(result) + str(ns[0])), ns[1:]))

    return possibles


def handle_part_1(lines: list[str]) -> int:
    equations = [
        (int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split())))
        for line in lines
    ]

    s = 0
    for test, numbers in equations:
        s += test if any(test == x for x in evaluate(numbers)) else 0
    return s


def handle_part_2(lines: list[str]) -> int:
    equations = [
        (int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split())))
        for line in lines
    ]

    s = 0
    for test, numbers in equations:
        s += test if any(test == x for x in evaluate(numbers, True)) else 0
    return s
