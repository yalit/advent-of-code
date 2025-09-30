def handle_part_1(lines: list[str]) -> int:
    states = {s: (tuple(map(lambda a: int(a) if a in ['0', '1', '-1'] else a, z.split(","))),tuple(map(lambda a: int(a) if a in ['0','1', '-1'] else a, o.split(",")))) for s, z, o in (line.split() for line in lines)}

    memory = {0: 0}
    state = 'A'
    cursor = 0

    nb_steps = 6 if len(states) == 2 else 12656374

    print(states)

    for _ in range(nb_steps):
        if cursor not in memory:
            memory[cursor] = 0
        write, move, next_state = states[state][memory[cursor]]
        memory[cursor] = write
        cursor += move
        state = next_state

    return sum(memory[cursor] for cursor in memory)


def handle_part_2(lines: list[str]) -> int:
    return 0
