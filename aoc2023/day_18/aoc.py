dirs = {'R' : (0,1), 'L': (0,-1), 'U':(-1,0), 'D':(1,0)}

def handle_part_1(lines: list[str]) -> int:
    edge = 0
    points = [(0,0)]

    for line in lines:
        r,c = points[-1]
        d, n, _ = line.split()

        for _ in range(int(n)):
            r,c= r + dirs[d][0], c + dirs[d][1]
            edge += 1
        points.append((r,c))

    return pick_value(edge, shoelace_area(points)) + edge


def handle_part_2(lines: list[str]) -> int:
    edge = 0
    points = [(0, 0)]
    color_directions = ['R', 'D', 'L', 'U']

    for line in lines:
        r, c = points[-1]
        _, _, color = line.replace("(", "").replace(")", "").replace('#', '').split()

        d = color_directions[int(color[-1])]
        n = int(color[:5], 16)

        for _ in range(int(n)):
            r, c = r + dirs[d][0], c + dirs[d][1]
            edge += 1
        points.append((r, c))

    return pick_value(edge, shoelace_area(points)) + edge

def shoelace_area(points: list[tuple[int, int]]):
    shoelace = zip(points, points[1:] + [points[0]])
    return int(abs(sum([(x1*y2) - (x2*y1) for (x1,y1), (x2,y2) in shoelace])/2))

def pick_value(nb_points, area):
    return area + 1 - int(nb_points / 2)
