def handle_part_1(lines: list[str]) -> int:
    rolls = set()

    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            if val == '@':
                rolls.add((row,col))

    total = 0
    for row,col in rolls:
        n = 0
        for dr in [-1, 0, 1]:
            for dc in [-1,0,1]:
                if dr == 0 and dc == 0: continue
                if (row+dr, col+dc) in rolls:
                    n+=1
        if n < 4:
            total+=1
    return total


def handle_part_2(lines: list[str]) -> int:
    rolls = set()

    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            if val == '@':
                rolls.add((row,col))

    total = 0
    moved = True
    while moved:
        moves = 0
        moved = False
        new_rolls = set()

        for row,col in rolls:
            n = 0
            for dr in [-1, 0, 1]:
                for dc in [-1,0,1]:
                    if dr == 0 and dc == 0: continue
                    if (row+dr, col+dc) in rolls:
                        n += 1
            if n < 4:
                total+=1
                moves+=1
            else:
                new_rolls.add((row,col))
        
        if moves > 0:
            moved = True
            rolls = new_rolls

    return total
