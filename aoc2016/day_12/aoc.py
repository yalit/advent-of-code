def playInstructions(registers, lines):
    instructions = list(map(lambda l: l.split(" "), lines))

    line = 0
    while line < len(instructions):
        ins = instructions[line]

        if ins[0] == "cpy":
            if ins[1] in registers:
                registers[ins[2]] = registers[ins[1]]
            else:
                registers[ins[2]] = int(ins[1])
            line += 1

        elif ins[0] == "inc":
            registers[ins[1]] += 1
            line += 1

        elif ins[0] == "dec":
            registers[ins[1]] -= 1
            line += 1

        elif ins[0] == "jnz":
            jump = int(ins[2])
            v = int(ins[1]) if ins[1] not in registers else registers[ins[1]]
            if v == 0:
                jump = 1
            line += jump
    return registers


def handle_part_1(lines: list[str]) -> int:
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}

    return playInstructions(registers, lines)["a"]


def handle_part_2(lines: list[str]) -> int:
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}

    return playInstructions(registers, lines)["a"]
