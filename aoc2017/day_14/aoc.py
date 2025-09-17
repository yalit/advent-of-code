from functools import reduce

def handle_part_1(lines: list[str]) -> int:
    nb = 0
    for i in range(128):
        nb += sum(list(map(int, hash(lines[0]+"-"+str(i)))))
    return nb


def handle_part_2(lines: list[str]) -> int:
    grid = []
    for i in range(128):
        grid.append(list(map(int, hash(lines[0]+"-"+str(i)))))

    counted = set()
    nb_regions = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 0:
                continue

            if (r,c) in counted:
                continue

            to_visit = [(r,c)]
            visited = set()
            while to_visit:
                tr,tc = to_visit.pop()

                if (tr,tc) in visited or (tr,tc) in counted:
                    continue

                for dr,dc in [(0,1), (0,-1),(1,0),(-1,0)]:
                    nr,nc = tr+dr, tc+dc
                    if 0 <= nr < 128 and 0 <= nc < 128 and grid[nr][nc] == 1:
                        to_visit.append((nr,nc))
                visited.add((tr,tc))
            nb_regions += 1
            counted = counted.union(visited)

    return nb_regions

def hash(input: str) -> list[str]:
    lengths = list(input.encode('utf-8')) + [17, 31, 73, 47, 23]
    pos,skip = 0, 0

    l = list(range(256))
    for _ in range(64):
        l, pos, skip = knot(l, lengths, pos, skip)

    hash = ""
    for i in range(16):
        sparse = l[16*i:16*(i+1)]
        dense = reduce(lambda h,x: h^x, sparse)
        hash += (hex(dense)[2:].zfill(2))


    return list("".join(list(map(lambda a: bin(int(a,16))[2:].zfill(4), hash))))

def knot(l, lengths, pos = 0, skip = 0) -> tuple[list[int], int, int]:
    for n in lengths:
        chunk = []
        if pos + n <= len(l):
            chunk = l[pos:pos+n]
        else: # near the end and need to circular bound
            end = len(l) - pos
            start = n-end
            chunk = l[pos:] + l[0:start]

        for i, x in enumerate(reversed(chunk)):
            l[(pos+i)%len(l)] = x

        pos = (pos + n + skip) % len(l)
        skip += 1

    return l, pos, skip
