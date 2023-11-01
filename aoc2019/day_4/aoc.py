def is_matching(nb: int) -> bool:
    c_n: int = -1
    all_increasing = True
    double = False
    for n_n in list(str(nb)):
        if int(n_n) == c_n:
            double = True
        if int(n_n) < c_n:
            all_increasing = False
        c_n = int(n_n)

    if double and all_increasing:
        return True

    return False

def is_matching_complex(nb: int) -> bool:
    c_n: int = -1
    all_increasing = True
    double_found = {}
    for n_n in list(str(nb)):
        i_n_n = int(n_n)
        if i_n_n == c_n:
            double_found[i_n_n] = True if i_n_n not in double_found else False
        if i_n_n < c_n:
            all_increasing = False
            break
        c_n = i_n_n

    double = False
    for k in  double_found.values():
        if k:
            double = True
    if double and all_increasing:
        return True

    return False

def handle_part_1(lines: list[str]) -> int:
    limits = lines[0].split('-')
    minimum = int(limits[0])
    maximum = int(limits[1])

    nb = 0
    for n in range(minimum, maximum + 1):
        nb += 1 if is_matching(n) else 0

    return nb


def handle_part_2(lines: list[str]) -> int:
    limits = lines[0].split('-')

    nb = 0
    for n in range(int(limits[0]), int(limits[1]) + 1):
        nb += 1 if is_matching_complex(n) else 0

    return nb
