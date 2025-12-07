def handle_part_1(lines: list[str]) -> int:
    splitters = set()
    start = None
    height = len(lines) - 1

    for row, line in enumerate(lines):
        for col, v in enumerate(line):
            if v == '^':
                splitters.add((row,col))
            if v == 'S':
                start = (row,col)

    beams = set([start])
    splits = 0
    while any(row < height for row,_ in beams):
        new_beams = set()

        for row,col in beams:
            nr = row+1
            if (nr,col) in splitters:
                new_beams.add((nr, col-1))
                new_beams.add((nr, col+1))
                splits += 1
            else:
                new_beams.add((nr,col))
        beams = set(new_beams)

    return splits



def handle_part_2(lines: list[str]) -> int:
    splitters = set()
    start = None
    height = len(lines)

    for row, line in enumerate(lines):
        for col, v in enumerate(line):
            if v == '^':
                splitters.add((row,col))
            if v == 'S':
                start = (row,col)


    beams = {start: 1}
    while any(row <= height for row,_ in beams.keys()):
        new_beams = {} 
        changed = False
        for (row,col), n in beams.items():
            nr = row+1
            if (nr,col) in splitters:
                if (nr,col-1) not in new_beams:
                    new_beams[(nr,col-1)] = 0
                if (nr,col+1) not in new_beams:
                    new_beams[(nr,col+1)] = 0
                new_beams[(nr,col-1)] += n
                new_beams[(nr,col+1)] += n
                changed = True
            else:
                if (nr,col) not in new_beams:
                    new_beams[(nr,col)] = 0
                new_beams[(nr,col)] += n

        beams = new_beams

    return sum(v for _, v in beams.items()) 
