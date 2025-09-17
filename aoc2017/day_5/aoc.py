def handle_part_1(lines: list[str]) -> int:
    memory = [int(x) for x in lines]
    s = 0
    i = 0

    while i < len(memory):
        d = memory[i]
        memory[i] = d+1
        i += d
        s+=1

    return s


def handle_part_2(lines: list[str]) -> int:
    memory = [int(x) for x in lines]
    s = 0
    i = 0

    while i < len(memory):
        d = memory[i]
        if d >= 3:
            memory[i] = d-1
        else:
            memory[i] = d+1
        i += d
        s+=1

    return s
