def handle_part_1(lines: list[str]) -> int:
    d= get_pipes(lines)
    group = get_group(d, 0)
    return len(group)


def handle_part_2(lines: list[str]) -> int:
    d= get_pipes(lines)

    visited = set()
    start = 0
    nb = 0

    while len(visited) < len(d):
        group = get_group(d, start)
        visited = visited.union(group)
        not_visited = [x for x in d.keys() if x not in visited]
        if len(not_visited) >= 1:
            start = not_visited[0]
        nb +=1

    return nb


def get_pipes(lines: list[str]):
    d = {}

    for l in lines:
        n, p = l.split(" <-> ")
        d[int(n)] = list(map(int, p.split(', ')))
    return d

def get_group(d, start):
    group = set()
    to_visit = [start]
    while to_visit:
        n = to_visit.pop()

        if n in group:
            continue

        for p in d[n]:
            to_visit.append(p)
        group.add(n)
    return group