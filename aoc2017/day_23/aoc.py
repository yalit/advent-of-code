from python.libraries.utils import isprime


def get_value(registers: dict[str, int], x: str) -> int:
    if x in registers:
        return registers[x]
    return int(x)

def operate(registers: dict[str, int], op: str, X: str, Y: str, step: int) -> int:
    delta_step = 1
    if op == "set":
        registers[X] = get_value(registers, Y)
    elif op == "sub":
        registers[X] -= get_value(registers, Y)
    elif op == "mul":
        registers[X] *= get_value(registers, Y)
    elif op == "jnz":
        if get_value(registers, X) != 0:
            delta_step = get_value(registers, Y)
    return step + delta_step

def handle_part_1(lines: list[str]) -> int:
    registers = {chr(c): 0 for c in range(ord('a'), ord('h') + 1)}
    nb_mult = 0
    step = 0
    operations = [line.split() for line in lines]

    while step < len(operations):
        op, X, Y = operations[step]
        step = operate(registers, op, X, Y, step)
        if op == "mul":
            nb_mult += 1

    return nb_mult


def handle_part_2(lines: list[str]) -> int:
    # Interpretation of the assembly code
    f = 57*100 + 100000
    t = f + 17000
    return len([h for h in range(f, t+1, 17) if isprime(h) is False])