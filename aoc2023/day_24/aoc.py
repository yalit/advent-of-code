from sympy import solve, Symbol, Eq


def handle_part_1(lines: list[str]) -> int:
    minimum = 200000000000000
    maximum = 400000000000000
    points = [list(map(int, line.replace(" @", ',').split(', '))) for line in lines]
    # point = (start_x, start_y, start_z, delta_x, delta_y, delta_z, a, b) for line equation as y = ax + b for each trajectory
    points = [p + [p[4] / p[3], p[1] - (p[4] / p[3] * p[0])] for p in points]

    nb_intersections = 0
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[i + 1:]):
            if p1[6] != p2[6]:
                x = (p1[7] - p2[7]) / (p2[6] - p1[6])
                y = (p1[6] * x) + p1[7]
                n1 = (x - p1[0]) / p1[3]
                n2 = (x - p2[0]) / p2[3]
                if n1 >= 0 and n2 >= 0:
                    if minimum <= x <= maximum and minimum <= y <= maximum:
                        nb_intersections += 1

    return nb_intersections


def handle_part_2(lines: list[str]) -> int:
    x = Symbol("x")
    y = Symbol("y")
    z = Symbol("z")
    dx = Symbol("dx")
    dy = Symbol("dy")
    dz = Symbol("dz")

    symbols = [x,y,z,dx,dy,dz]
    equations = []
    # point = (start_x, start_y, start_z, delta_x, delta_y, delta_z)
    points = [list(map(int, line.replace(" @", ',').split(', '))) for line in lines]

    for i, point in enumerate(points[:3]): # only need 3 points to ensure alignment => chech done if same results with 9 / 10 & 20 points
        ni = Symbol('n' + str(i))
        symbols.append(ni)
        equations.append(Eq((x + ni * dx - point[0] - ni * point[3]),0))
        equations.append(Eq((y + ni * dy - point[1] - ni * point[4]), 0))
        equations.append(Eq((z + ni * dz - point[2] - ni * point[5]), 0))

    solution = solve(tuple(equations), tuple(symbols))

    return solution[0][0] + solution[0][1] + solution[0][2]
