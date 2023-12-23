from heapq import heappush, heappop
from collections import deque

def handle_part_1(lines: list[str]) -> int:
    _, supports, supported_by = make_blocks_fall(lines)

    return len([i for i, supported in supports.items() if len(supported) == 0
                or len([x for x, support in supported_by.items() if i in support and len(support) == 1]) == 0])

def handle_part_2(lines: list[str]) -> int:
    placed_elements, supports, supported_by = make_blocks_fall(lines)

    disintegratable = [i for i, supported in supports.items() if len(supported) == 0
                or len([x for x, support in supported_by.items() if i in support and len(support) == 1]) == 0]

    non_disintegratable_elements = []
    for x in [e for e in placed_elements if e[3] not in disintegratable]:
        heappush(non_disintegratable_elements, x)

    fallable_bricks = {x: set() for _, _, _, x in non_disintegratable_elements}

    while len(non_disintegratable_elements) > 0:
        _, _, _, i = heappop(non_disintegratable_elements)

        to_fall = list(supports[i])
        while to_fall:
            falling = to_fall.pop()
            fallable_bricks[i].add(falling)

            for block in supports[falling]:
                # if falling falls does it make fall the blocks it supports
                # yes if he is the only one supporting the block in question
                if len(supported_by[block]) == 1:
                    to_fall.append(block)
                else:
                    supported_by[block].remove(falling)

    return sum([len(n) for x, n in fallable_bricks.items()])

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