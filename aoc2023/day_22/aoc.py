from heapq import heappush, heappop
from collections import deque

def handle_part_1(lines: list[str]) -> int:
    _, supports, supported_by = make_blocks_fall(lines)

    return len([i for i, supported in supports.items() if len(supported) == 0
                or len([x for x, support in supported_by.items() if i in support and len(support) == 1]) == 0])

def handle_part_2(lines: list[str]) -> int:
    placed_elements, supports, supported_by = make_blocks_fall(lines)

    total = 0
    for _, _, _, i in placed_elements:
        sole_supported = deque(x for x in supports[i] if len(supported_by[x]) == 1) # all elements only supported by i
        falling = set(sole_supported)
        falling.add(i)

        while sole_supported:
            x = sole_supported.popleft()
            for e in supports[x] - falling:
                if supported_by[e] <= falling:
                    sole_supported.append(e)
                    falling.add(e)
        total += len(falling) - 1

    return total

def make_blocks_fall(lines):
    sorted_elements = []
    elements = {}
    # element = (z, (minX, maxX), (minY, maxY))
    # one heapQueue sorted on the z axis of all the elements
    # one dictionary of all the elements with the number of elements they support
    supported_by = {}
    supports = {}

    for i, line in enumerate(lines):
        f, t = line.split('~')
        fx, fy, fz = f.split(',')
        tx, ty, tz = t.split(',')
        heappush(sorted_elements, (
        (min(int(fz), int(tz)), max(int(fz), int(tz))), (min(int(fx), int(tx)), max(int(fx), int(tx))),
        (min(int(fy), int(ty)), max(int(fy), int(ty))), i))
        elements[i] = (min(int(fz), int(tz)), max(int(fz), int(tz))), (min(int(fx), int(tx)), max(int(fx), int(tx))), (
        min(int(fy), int(ty)), max(int(fy), int(ty)))
        supports[i] = set()
        supported_by[i] = set()

    # placed elements
    placed_elements = []

    while sorted_elements:
        (minZ, maxZ), (minX, maxX), (minY, maxY), i = heappop(sorted_elements)

        if minZ == 1:
            heappush(placed_elements, ((minZ, maxZ), (minX, maxX), (minY, maxY), i))
            continue

        minZ -= 1
        maxZ -= 1
        # check for all elements in placed_elements that there is none merged with the x/y
        blocked = False
        for (pminZ, pmaxZ), (pminX, pmaxX), (pminY, pmaxY), pi in [placed_element for placed_element in placed_elements
                                                                   if placed_element[0][1] == minZ]:

            if (maxX >= pminX and minX <= pmaxX) and (maxY >= pminY and minY <= pmaxY):  # blocked by the current element
                blocked = True

                supports[pi].add(i)
                supported_by[i].add(pi)

        if blocked:
            heappush(placed_elements, ((minZ + 1, maxZ + 1), (minX, maxX), (minY, maxY), i))
        else:
            heappush(sorted_elements, ((minZ, maxZ), (minX, maxX), (minY, maxY), i))

    return placed_elements, supports, supported_by