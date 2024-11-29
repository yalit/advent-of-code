def play_instructions(registers, lines):
    instructions = list(map(lambda l: l.split(" "), lines))
    outs = []
    outs_state = []

    def get_value(a: str):
        if a in registers:
            return registers[a]
        else:
            return int(a)

    line = 0
    while line < len(instructions):
        ins = instructions[line]

        if ins[0] == "cpy":
            if ins[2] in registers:
                registers[ins[2]] = get_value(ins[1])
            line += 1

        elif ins[0] == "jnz":
            jump = get_value(ins[2])
            v = get_value(ins[1])
            if v == 0:
                jump = 1
            line += jump

        elif ins[0] == "inc":
            registers[ins[1]] += 1
            line += 1

        elif ins[0] == "dec":
            registers[ins[1]] -= 1
            line += 1

        elif ins[0] == "out":
            value = get_value(ins[1])
            outs.append(value)
            state = (value, registers)
            outs_state.append(state)

            if len(outs) > 1 and outs[-2] == outs[-1]:
                return False

            if (
                len(outs) > 100
                and outs[-1] == outs[-3]
                and outs_state[-1] == outs_state[-3]
                and outs[-2] == outs[-4]
                and outs_state[-2] == outs_state[-4]
                and outs[0] == 0
            ):
                print(outs)
                for s in outs_state:
                    print(s)
                return True

            line += 1
    return registers


def handle_part_1(lines: list[str]) -> int:
    registers = {"a": -1, "b": 0, "c": 0, "d": 0}
    found = False
    n = -1
    while not found:
        n += 1
        registers = {"a": n, "b": 0, "c": 0, "d": 0}
        found = play_instructions(registers, lines)
        print(n, found)
    return n


def handle_part_2(lines: list[str]) -> int:
    return 0
