def handle_part_1(lines: list[str]) -> int:
    n = int(lines[0])
    r = int(n**0.5) if int(n**0.5) % 2 == 0 else int(n**0.5) + 1
    p = r ** 2
    d = (r+1)**2 - n

    # just because I saw that d is always less than r for the value
    x, y = r-d, r

    return abs(x-r//2)+abs(y-r//2)


def handle_part_2(lines: list[str]) -> int:
    n = int(lines[0])
    v = 1
    r = 1
    x,y = 0,0
    points = {(0,0): 1}

    while v <= n:
        for dx, dy in get__path_directions(r):
            x, y = x+dx,y+dy
            v =  get_sum_neighbors(points, x, y)    
            points[(x,y)] = v
            print((x,y), v, n)
            if v > n:
                break

        r += 1

    display(points)
    return v 

def get_sum_neighbors(points, x,y):
    s = 0
    for dx, dy in [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1, 1)]:
        if (x+dx, y+dy) in points:
            s += points[(x+dx, y+dy)]

    return s

def get__path_directions(n: int): 
    dirs = [(1,0)]

    dirs = dirs + [(0,-1) for _ in range(n*2 - 1)]
    dirs = dirs + [(-1,0) for _ in range(n*2)]
    dirs = dirs + [(0,1) for _ in range(n*2)]
    dirs = dirs + [(1,0) for _ in range(n*2)]

    return dirs

def display(points):
    min_x = min([x for x,_ in points.keys()])
    min_y = min([y for _,y in points.keys()])
    max_x = max([x for x,_ in points.keys()])
    max_y = max([y for _,y in points.keys()])
    m = max([x for x in points.values()])
    l = len(str(m))

    for y in range(min_y, max_y+1):
        r = []
        for x in range(min_x, max_x + 1):
            if (x,y) in points:
                r.append(points[(x,y)])
            else:
                r.append("")
        print(" ".join([" "*(l-len(str(x))) + str(x) for x in r]))