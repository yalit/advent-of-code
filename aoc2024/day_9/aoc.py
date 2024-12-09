import time

def handle_part_1(lines: list[str]) -> int:
    start = time.time()
    dm = lines[0]
    checksum = 0
    nb = sum([int(dm[x]) for x in range(0, len(dm), 2)])

    id_bottom = 0
    id_top = len(dm) // 2
    pos_bottom = 0
    pos_top = len(dm) - 1 if len(dm) % 2 != 0 else len(dm) - 2
    top = 0
    position = 0

    visualization = ""
    while position < nb:
        for _ in range(int(dm[pos_bottom])):
            if position >= nb:
                break
            if pos_bottom% 2 == 0:  # pick bottom
                checksum += position * id_bottom
                visualization += str(id_bottom)
            else:
                top += 1
                checksum += position * id_top
                visualization += str(id_top)
                if not (top < int(dm[pos_top])):
                    id_top -= 1
                    pos_top -= 2
                    top = 0
            position += 1
        if pos_bottom % 2 == 0:
            id_bottom += 1
        pos_bottom += 1

    print("Part 1: ", time.time() - start, "s")
    return checksum


def handle_part_2(lines: list[str]) -> int:
    start = time.time()
    dm = lines[0]
    checksum = 0 # the first part has an id of 0 so always for the first positioned element

    max_id = len(dm) // 2
    top = len(dm) - 1 if len(dm) % 2 != 0 else len(dm) - 2
    pos_dm = 1
    id_bottom = 1
    position = int(dm[0])
    positioned = {0}
    visualization = "".join(["0" for _ in range(int(dm[0]))])
    swapped_positions = {}

    while len(positioned) <= max_id:
        if pos_dm % 2 == 0:
            if position in swapped_positions:
                nb = swapped_positions[position]
                position += nb
                visualization += "".join(["." for _ in range(nb)])
            else:
                checksum += sum(id_bottom * (position+x) for x in range(int(dm[pos_dm])))
                visualization += "".join([str(id_bottom) for _ in range(int(dm[pos_dm]))])
                position += int(dm[pos_dm])
                positioned.add(id_bottom)
            id_bottom += 1
        else:
            size_available = int(dm[pos_dm])
            while True:
                found = False
                for i, x in enumerate(range(top, 0, -2)):
                    if int(dm[x]) <= size_available and max_id-i not in positioned:
                        checksum += sum((max_id-i) * (position+y) for y in range(int(dm[x])))
                        visualization += "".join([str(max_id-i) for _ in range(int(dm[x]))])
                        supposed_position = sum(int(x) for x in dm[:x])
                        swapped_positions[supposed_position] = int(dm[x]) # position starts from 0
                        position += int(dm[x])
                        positioned.add(max_id-i)
                        size_available -= int(dm[x])
                        found = True
                        break
                if not found or size_available == 0:
                    position += size_available
                    visualization += "".join(["." for _ in range(size_available)])
                    break
        pos_dm+=1

    print("Part 2: ", time.time() - start, "s")
    return checksum
