from heapq import heappush, heappop
from python.libraries.array import inbound
from python.libraries.utils import directNeighbors


def handle_part_1(lines: list[str]) -> int:
    return handle(lines, 3)

def handle_part_2(lines: list[str]) -> int:
    return handle(lines, 10, 4)

def handle(lines, max_same, min_same = 1):
    lines = [[int(n) for n in row] for row in lines]
    h = len(lines)
    w = len(lines[0])
    end = (h - 1, w - 1)

    heap = [(0,0,0,0,0,0)] #heatloss, row, col,dr,dc,nb times same

    visited = set()

    while len(heap) > 0:
        hl,r,c,dr,dc,nb = heappop(heap)

        if (r,c) == end and nb >= min_same:
            return hl

        if (r,c,dr,dc,nb) in visited:
            continue

        visited.add((r,c,dr,dc,nb))

        #going same direction
        if nb < max_same and (dr,dc) != (0,0):
            next_r = r + dr
            next_c = c + dc
            if inbound(next_r, next_c, h, w):
                heappush(heap,(hl + lines[next_r][next_c], next_r, next_c, dr, dc, nb + 1))

        #trying all directions but the same and the reverse
        if nb >= min_same or (dr,dc) == (0,0):
            for next_dr, next_dc in directNeighbors:
                if (next_dr, next_dc) != (dr, dc) and (next_dr, next_dc) != (-dr, -dc):
                    next_r = r + next_dr
                    next_c = c + next_dc
                    if inbound(next_r, next_c, h, w):
                        heappush(heap, (hl + lines[next_r][next_c], next_r, next_c, next_dr, next_dc, 1))

    return -1