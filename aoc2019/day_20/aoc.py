from python.libraries.array import visualize, visualize_grid_dict
from python.libraries.utils import directNeighbors


def get_grid_and_portals(lines):
    w = max([len(x) for x in lines])
    h = len(lines)
    portals = {}
    outer_or_inner = {}

    def add_to_portals(x, y, v, o_i):
        if v not in portals:
            portals[v] = []
        portals[v].append((x, y))
        outer_or_inner[(v, (x,y))] = o_i

    # top portals
    for x, v in enumerate(lines[0]):
        if not v.isalpha():
            continue
        add_to_portals(x, 2, v + lines[1][x], 'outer')
    # bottom portals
    for x, v in enumerate(lines[-2]):
        if not v.isalpha():
            continue
        add_to_portals(x, h - 3, v + lines[-1][x], 'outer')
    # left portals
    for y in range(h-2):
        if not lines[y][0].isalpha():
            continue
        add_to_portals(2, y, lines[y][0] + lines[y][1], 'outer')
    # right portals
    for y in range(h-2):
        if not lines[y][-2].isalpha():
            continue
        add_to_portals(w - 3, y, lines[y][-2] + lines[y][-1], 'outer')


    grid = set()
    for y in range(2, h-2):
        l = lines[y]
        for x in range(2, w-2):
            v = l[x]
            if v == '.':
                grid.add((x, y))
            if v.isalpha():
                # left inner
                if x-1 >=0 and x+1 < w and l[x - 1] in ['.', '#'] and l[x + 1].isalpha():
                    add_to_portals(x - 1, y, v + l[x + 1], 'inner')

                # right inner
                elif x+2 < w and l[x + 2] in ['.', '#'] and l[x + 1].isalpha():
                    add_to_portals(x + 2, y, v + l[x + 1], 'inner')

                # top inner
                elif y-1>=0 and y+1 < w and lines[y - 1][x] in ['.', '#'] and lines[y + 1][x].isalpha():
                    add_to_portals(x, y - 1, v + lines[y + 1][x], 'inner')

                # bottom inner
                elif y+2 < w and lines[y + 2][x] in ['.', '#'] and lines[y + 1][x].isalpha():
                    add_to_portals(x, y + 2, v + lines[y + 1][x], 'inner')

    return grid, portals, outer_or_inner

def is_portal(portals, pos):
    for k, v in portals.items():
        if pos in v:
            return k
    return None

def get_portals_around(grid, portals):
    portal_arounds = {}
    for p, v in portals.items():
        for position in v:
            portal_arounds[(p, position)] = []
            to_visit = [(position, 0)]
            visited = set()

            while to_visit:
                pos, steps = to_visit.pop(0)
                portal = is_portal(portals, pos)
                if portal is not None and portal != p:
                    portal_arounds[(p, position)].append(((portal, pos), steps))
                    continue
                x, y = pos
                for dx, dy in directNeighbors:
                    new_pos = (x + dx, y + dy)
                    if new_pos not in grid or new_pos in visited:
                        continue
                    to_visit.append((new_pos, steps + 1))
                visited.add(pos)
    return portal_arounds

def handle_part_1(l: list[str]) -> int:
    w = max([len(x) for x in l])
    lines = [list(x.ljust(w)) for x in l]
    visualize(lines)

    grid, portals, _ = get_grid_and_portals(lines)
    portals_around = get_portals_around(grid, portals)


    def score(from_position, positions_traveled, distance):
        if from_position == ('ZZ', portals['ZZ'][0]):
            return distance

        portaled_position = from_position
        portal_cost = 0
        if from_position[0] != 'AA':
            portaled_position = (from_position[0], portals[from_position[0]][1 - portals[from_position[0]].index(from_position[1])])
            portal_cost = 1

        next_positions = [(p, s) for p, s in portals_around[portaled_position] if p not in positions_traveled]
        if not next_positions:
            return float('inf')
        return min([score(p, positions_traveled[:] + [from_position], distance + s + portal_cost) for p, s in next_positions])

    return score(('AA', portals['AA'][0]), [],0)


def handle_part_2(l: list[str]) -> int:
    w = max([len(x) for x in l])
    lines = [list(x.ljust(w)) for x in l]
    visualize(lines)

    grid, portals, outer_or_inner = get_grid_and_portals(lines)
    portals_around = get_portals_around(grid, portals)

    for k, v in portals.items():
        print(f"Portal {k}: is at {v}")

    memoization = {}

    def score(from_position, positions_traveled, distance):
        key_from_position = (from_position[0], from_position[1])
        if key_from_position == ('ZZ', portals['ZZ'][0]):
            if from_position[2] == 0:
                return distance
            return float('inf')

        if from_position[2] >= 100 or from_position[2] < 0:
            return float('inf')

        if distance >= 7500:
            return float('inf')

        if (from_position, tuple(positions_traveled)) in memoization:
            return memoization[(from_position, tuple(positions_traveled))]

        portaled_position = key_from_position
        portal_cost = 0
        next_level = 1
        if from_position[0] != 'AA':
            portaled_position = (
                from_position[0],
                portals[from_position[0]][1 - portals[from_position[0]].index(from_position[1])],
            )
            portal_cost = 1
            next_level = from_position[2] + (1 if outer_or_inner[key_from_position] == 'inner' else -1)

        next_positions = [(p, s) for p, s in portals_around[portaled_position] if p not in positions_traveled]

        if not next_positions:
            return float('inf')

        s = min(
            [score(
                p + (next_level,),
                positions_traveled[:] + [from_position],
                distance + s + portal_cost
            ) for p, s in next_positions])

        memoization[(from_position, tuple(positions_traveled))] = s
        return s

    return score(('AA', portals['AA'][0], 0), [], 0)
