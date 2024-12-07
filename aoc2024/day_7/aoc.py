def evaluate(test, numbers, join=False):
    to_test = [(test, numbers)]
    while to_test:
        n_test, ns = to_test.pop()

        if len(ns) == 0 and n_test == 0:
            return True

        if len(ns) == 0:
            continue

        last = ns[-1]
        next = ns[:-1]
        # test *
        if n_test % last == 0:
            to_test.append((n_test // last, next))

        # test +
        if n_test >= last:
            to_test.append((n_test - last, next))

        # test || if join
        s_last = str(last)
        s_n_test = str(n_test)
        if join:
            if s_n_test == s_last:
                return True
            elif s_n_test.endswith(s_last):
                to_test.append((int(s_n_test[: -len(s_last)]), next))

    return False


def handle_part_1(lines: list[str]) -> int:
    equations = [
        (int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split())))
        for line in lines
    ]

    s = 0
    for test, numbers in equations:
        s += test if evaluate(test, numbers) else 0
    return s


def handle_part_2(lines: list[str]) -> int:
    equations = [
        (int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split())))
        for line in lines
    ]

    s = 0
    for test, numbers in equations:
        s += test if evaluate(test, numbers, True) else 0
    return s
