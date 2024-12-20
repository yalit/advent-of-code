from python.libraries.utils import euclidian_distance

def handle_part_1(lines: list[str]) -> int:
    nodes = set([(r,c) for r, row in enumerate(lines) for c, cell in enumerate(row) if cell == '.' or cell == 'E' or cell == 'S'])
    walls = set([(r+1,c+1) for r, row in enumerate(lines[1:-1]) for c, cell in enumerate(row[1:-1]) if cell == '#'])
    start = [(r,c) for r, row in enumerate(lines) for c, cell in enumerate(row) if cell == 'S'][0]
    end = [(r,c) for r, row in enumerate(lines) for c, cell in enumerate(row) if cell == 'E'][0]

    path = {start: 0}
    current = start
    i = 1
    while current != end:
        for next_current in [(current[0]+1, current[1]), (current[0]-1, current[1]), (current[0], current[1]+1), (current[0], current[1]-1)]:
            if next_current in nodes and next_current not in path:
                path[next_current] = i
                i+=1
                current = next_current

    saved = []
    for r,c in walls:
        if (r,c+1) in path and (r,c-1) in path:
            saved.append((r,c,abs(path[(r,c+1)] - path[(r,c-1)]) - 2))

        elif (r+1,c) in path and (r-1,c) in path:
            saved.append((r,c,abs(path[(r+1,c)] - path[(r-1,c)]) - 2))

    return len([s for s in saved if s[2] >= 100])


def handle_part_2(lines: list[str]) -> int:
    nodes = [(r, c) for r, row in enumerate(lines) for c, cell in enumerate(row) if
                 cell == '.' or cell == 'E' or cell == 'S']
    start = [(r, c) for r, row in enumerate(lines) for c, cell in enumerate(row) if cell == 'S'][0]
    end = [(r, c) for r, row in enumerate(lines) for c, cell in enumerate(row) if cell == 'E'][0]

    path_index = {start: 0}
    path = [start]
    current = start
    i = 1
    while current != end:
        for next_current in [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1),
                             (current[0], current[1] - 1)]:
            if next_current in nodes and next_current not in path_index:
                path_index[next_current] = i
                path.append(next_current)
                i += 1
                current = next_current
    path.append(end)

    max_cheat = 20
    threshold = 100
    nb_cheats_above_threshold = 0
    for i, current in enumerate(path):
        found_cheats = set()
        # i+ threshold + 2 because we need to check only the nodes that are at least threshold +2 away from the current node (those are the ones that fits the condition)
        for to_be_checked in [tbc for tbc in path[i+threshold+2:] if euclidian_distance(current, tbc) <= max_cheat]:
            cheat = euclidian_distance(current, to_be_checked)
            if abs(path_index[current] - path_index[to_be_checked]) - cheat >= threshold:
                found_cheats.add(to_be_checked)
        nb_cheats_above_threshold += len(found_cheats)

    return nb_cheats_above_threshold




























