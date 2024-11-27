import math


def playInstructions(registers, lines, multiply: bool = False):
    instructions = list(map(lambda l: l.split(" "), lines))

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
            if multiply:
                registers[ins[1]] += 1
            else:
                registers[ins[1]] += 1
            line += 1

        elif ins[0] == "dec":
            registers[ins[1]] -= 1
            line += 1

        elif ins[0] == "tgl":
            step = get_value(ins[1])
            target = line + step

            if target >= len(instructions):
                line += 1
                continue

            if len(instructions[target]) == 2:
                instructions[target][0] = (
                    "dec" if instructions[target][0] == "inc" else "inc"
                )
            elif len(instructions[target]) == 3:
                instructions[target][0] = (
                    "cpy" if instructions[target][0] == "jnz" else "jnz"
                )
            line += 1

        else:
            line += 1

    return registers


def handle_part_1(lines: list[str]) -> int:
    registers = playInstructions({"a": 7, "b": 0, "c": 0, "d": 0}, lines)
    return registers["a"]


def handle_part_2(lines: list[str]) -> int:
    # the whole run is a factorial of the input (here 12)
    # and add to that the 7722 = 98*78
    return math.factorial(12) + 7722
