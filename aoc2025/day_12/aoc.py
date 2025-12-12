from functools import cache

def handle_part_1(lines: list[str]) -> int:
    lines = "\\".join(lines).split('\\\\')

    shapes = []
    for s in [tuple(tuple(b for b in block.split('\\')[1:])) for block in lines[:-1]]:
        shape = set()
        for r in range(3):
            for c in range(3):
                if s[r][c] == '#': shape.add((r,c))
        shapes.append(tuple(shape))

    combinations = {tuple(shape): all_combinations(shape) for shape in shapes}

    total = 0
    for area in lines[-1].split('\\'):
        size, n_shapes = area.split(': ')
        w, h = list(map(int, size.split('x')))
        to_fit = []
        for i,n in enumerate(n_shapes.split()):
            for a in range(int(n)):
                to_fit.append(shapes[i])

        # not enough space by default to fit them all...
        if sum(len(x) for x in to_fit) > w * h: 
            continue
        
        # anyway enough space to fit them all...
        if w * h >= len(to_fit) * 9:
            total += 1
            continue

        @cache
        def is_possible(placements, area, w, h):
            if all(x is not None for x in placements): return True
            
            n = placements.index(None)
            shape = to_fit[n]
            
            for row in range(h-3):
                for col in range(w-3):
                    if (row, col) in area: continue

                    for comb in combinations[shape]:
                        if not can_fit(comb, area, w, h, row, col): continue
                        placed = is_possible(tuple(v if i != n else (row, col) for i, v in enumerate(placements)), place(comb, area, row, col), w, h)
                        if placed: return True
                        
            return False
        
        placed = is_possible(tuple(None for _ in to_fit), (), w, h)
        total += 1 if place else 0

    return total


def handle_part_2(lines: list[str]) -> int:
    return 0


def can_fit(shape, area, w,h, row, col):
    for r,c in shape:
        if (row+r, col+c) in area: return False

    return True

def place(shape, area, row, col):
    for r,c in shape:
        if (row+r, col+c) in area: return area

    return area + tuple((row+r, col+c) for r,c in shape)

def flip_h(shape):
    return tuple([(2-r,c) for r,c in shape])

def flip_v(shape):
    return tuple([(r,2-c) for r,c in shape])

def rotate(shape):
    t = {(0,0): (0,1), (0,1): (0,2), (0,2): (1,2), (1,2): (2,2), (2,2): (2,1), (2,1): (2,0), (2,0): (1,0), (1,0): (0,0), (1,1): (1,1)}

    return tuple([t[x] for x in shape])

def all_combinations(shape):
    combinations = set([tuple(shape), tuple(flip_v(shape)), tuple(flip_h(shape))])

    # all rotations on the right
    t = shape
    for _ in range(4):
        t = rotate(t)
        combinations.add(tuple(t))

    t = flip_v(shape)
    for _ in range(4):
        t = rotate(t)
        combinations.add(tuple(t))

    t = flip_h(shape)
    for _ in range(4):
        t = rotate(t)
        combinations.add(tuple(t))

    return tuple(combinations)

