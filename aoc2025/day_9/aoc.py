def handle_part_1(lines: list[str]) -> int:
    tiles = [list(map(int, line.split(','))) for line in lines]

    largest = 0
    for i, a in enumerate(tiles):
        for b in tiles[i+1:]:
            largest = max(largest, area(a,b))

    return largest

def handle_part_2(lines: list[str]) -> int:
    tiles = sorted([list(map(int, line.split(','))) for line in lines])
    
    edges = set()
    edges_row = {}
    edges_col = {}

    for x,y in tiles:
        # corner which is on the same row
        row_corner = [(a,b) for a,b in tiles if b == y and a != x][0]
        # corner which is on the  same column
        col_corner = [(a,b) for a,b in tiles if b != y and a == x][0]

        for a in f_range(min(x, row_corner[0]), max(x, row_corner[0])+0.5, 0.5):
            edges.add((a,y))
            if y not in edges_row:
                edges_row[y] =set() 
            if a not in edges_col:
                edges_col[a] = set()
            edges_col[a].add(y)
            edges_row[y].add(a)
        for b in f_range(min(y, col_corner[1]), max(y, col_corner[1])+0.5, 0.5):
            edges.add((x,b))
            if b not in edges_row:
                edges_row[b] = set()
            if x not in edges_col:
                edges_col[x] = set()
            edges_col[x].add(b)
            edges_row[b].add(x)

    largest = 0

    for i, (a,b) in enumerate(tiles):
        for j in range(len(tiles)-1, i, -1):
            c,d = tiles[j]

            if area((a,b), (c,d)) <= largest: continue

            # what's the inner rectangle of the rectangle
            lx = min(a,c) + 0.5
            hx = max(a,c) - 0.5
            ly = min(b,d) + 0.5
            hy = max(b,d) - 0.5
            # check if the corners are all in
            if not is_inside((lx,ly), edges_row, edges_col): continue
            if not is_inside((lx,hy), edges_row, edges_col): continue
            if not is_inside((hx,ly), edges_row, edges_col): continue
            if not is_inside((hx,hy), edges_row, edges_col): continue
            
            # check if on each of the sides there is no edges (if yes it means that the rectangle is not full)
            if len([1 for x in edges_row[ly] if lx < x < hx]) > 0: continue
            if len([1 for x in edges_row[hy] if lx < x < hx]) > 0: continue
            if len([1 for y in edges_col[lx] if ly < y < hy]) > 0: continue
            if len([1 for y in edges_col[hx] if ly < y < hy]) > 0: continue

            # if all True then it's a valid rectangle
            largest = max(largest, area((a,b), (c,d)))

    return largest

def dist(a,b):
    return abs(a[0]-b[0]+1) + abs(a[1]-b[1]+1)

def area(a,b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

def is_inside(p, edges_row, edges_col):
    return sum(1 for x in edges_row[p[1]] if x >=0 and x < p[0]) %2 == 1 and sum(1 for y in edges_col[p[0]] if y >=0 and y < p[1]) %2 == 1

def f_range(s, e, d):
    while s < e:
        yield s
        s += d
