def handle_part_1(lines: list[str]) -> int:
    memory = [int(x) for x in lines[0].split()]

    steps = 0
    visions = set()
    print(mem_id(memory))
    while mem_id(memory) not in visions:
        visions.add(mem_id(memory))

        m = max(memory)
        i = memory.index(m)
        memory[i] = 0
        for x in range(1, m+1):
            memory[(i+x) % len(memory)] += 1 

        steps += 1
    return steps


def handle_part_2(lines: list[str]) -> int:
    memory = [int(x) for x in lines[0].split()]

    steps = 0
    visions = {}
    
    while mem_id(memory) not in visions:
        visions[mem_id(memory)] = steps

        m = max(memory)
        i = memory.index(m)
        memory[i] = 0
        for x in range(1, m+1):
            memory[(i+x) % len(memory)] += 1 

        steps += 1
    return steps - visions[mem_id(memory)]


def mem_id(m):
    return ",".join([str(x) for x in m])