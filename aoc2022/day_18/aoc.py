from functools import reduce

neighbors = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def handle_part_1(lines: list[str]) -> int:
    cubes = set([tuple(map(int, line.split(','))) for line in lines])

    nbSidesNotConnected = 0
    for cx, cy, cz in cubes:
        for nx, ny, nz in neighbors:
            nbSidesNotConnected += 1 if (cx + nx, cy + ny, cz + nz) not in cubes else 0

    return nbSidesNotConnected


def handle_part_2(lines: list[str]) -> int:
    cubes = set([tuple(map(int, line.split(','))) for line in lines])
    minimums = (reduce(min, [a[0] for a in cubes]), reduce(min, [a[1] for a in cubes]), reduce(min, [a[2] for a in cubes]))
    maximums = (reduce(max, [a[0] for a in cubes]), reduce(max, [a[1] for a in cubes]), reduce(max, [a[2] for a in cubes]))

    print(minimums, maximums)

    def isOutside(ox, oy, oz):
        allOnX = [a[0] for a in cubes if a[1] == oy and a[2] == oz]
        allOnY = [a[1] for a in cubes if a[0] == ox and a[2] == oz]
        allOnZ = [a[2] for a in cubes if a[1] == oy and a[0] == ox]
        if len(allOnX) == 0 or len(allOnY) == 0 or len(allOnZ) == 0:
            return True

        return canReachOutside(ox, oy, oz)

    def canReachOutside(cx, cy, cz):
        visited = set()
        toVisit = {(cx, cy, cz)}
        canDoIt = False
        while toVisit and not canDoIt:
            tx, ty, tz = toVisit.pop()
            for tnx, tny, tnz in neighbors:
                if (tx+tnx, ty+tny, tz+tnz) in visited or (tx+tnx, ty+tny, tz+tnz) in cubes:
                    continue

                if tx + tnx <= minimums[0] - 1 or tx + tnx >= maximums[0] + 2 or ty + tny <= minimums[1] - 1 or ty + tny >= maximums[1] + 2 or tz + tnz <= minimums[2] - 1 or tz + tnz >= maximums[2] + 2:
                    canDoIt = True
                    break

                toVisit.add((tx + tnx, ty + tny, tz + tnz))

            visited.add((tx, ty, tz))

        return canDoIt

    surface = 0
    # Assumption that the lava droplet is fully closed...
    # looking from the outside for any non lava droplet and count the surface touching lava
    for x in range(minimums[0] - 1, maximums[0] + 2):
        for y in range(minimums[1] - 1, maximums[1] + 2):
            for z in range(minimums[2] - 1, maximums[2] + 2):
                if (x, y, z) in cubes:
                    continue

                nbConnections = 0
                for nx, ny, nz in neighbors:
                    nbConnections += 1 if (x + nx, y + ny, z + nz) in cubes else 0

                if nbConnections == 0:
                    continue

                if isOutside(x, y, z):
                    surface += nbConnections

    return surface
