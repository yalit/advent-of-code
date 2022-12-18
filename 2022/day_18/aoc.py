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

        minX = reduce(min, allOnX)
        maxX = reduce(max, allOnX)
        minY = reduce(min, allOnY)
        maxY = reduce(max, allOnY)
        minZ = reduce(min, allOnZ)
        maxZ = reduce(max, allOnZ)

        outside = any([ox <= minX, ox >= maxX, oy <= minY, oy >= maxY, oz <= minZ or oz >= maxZ])

        if outside:
            return True

        return canGoOutside(x,y,z)


    def canGoOutside(x, y, z):
        visited = set()
        toVisit = {(x, y, z)}
        canReachOutside = False
        while toVisit and not canReachOutside:
            tx, ty, tz = toVisit.pop()
            for nx, ny, nz in neighbors:
                if (nx, ny, nz) in visited:
                    continue

                if tx + nx <= minimums[0] - 1 or tx + nx >= maximums[0] + 2 or ty + ny <= minimums[1] - 1 or ty + ny >= maximums[1] + 2 or tz + nz <= minimums[2] - 1 or tz + nz >= maximums[2] + 2:
                    canReachOutside = True
                    break

                toVisit.add((tx + nx, ty + ny, tz + nz))

            visited.add((tx, ty, tz))

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
