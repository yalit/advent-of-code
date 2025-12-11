from collections import deque
import functools

def handle_part_1(lines: list[str]) -> int:
    racks = {line.split(': ')[0]: line.split(': ')[1].split() for line in lines}

    total = 0
    to_visit = deque([("you",)])
    visited = set()

    while to_visit:
        path = to_visit.popleft()
        rack = path[-1]

        if rack == "out":
            total += 1
            continue

        if path in visited:
            continue

        for r in racks[rack]:
            to_visit.append(path+(r,))

        visited.add(path)


    return total

def handle_part_2(lines: list[str]) -> int:
    racks = {line.split(': ')[0]: line.split(': ')[1].split() for line in lines}
    if "out" not in racks:
        racks["out"] = []

    known = {}

    def get_nb_paths(start, finish, dac = False, fft= False):
        if (start, finish, dac, fft) in known:
            return known[(start,finish, dac, fft)]

        if start == finish:
            if dac and fft: return 1
            return 0

        total = 0
        for n in racks[start]:
            total += get_nb_paths(n, finish, dac or n == "dac", fft or n == "fft")

        known[(start, finish, dac, fft)] = total
        return total

    return get_nb_paths("svr", "out")

