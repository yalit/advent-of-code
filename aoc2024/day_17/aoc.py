import time


def get_registers_and_instructions(lines: list[str]) -> tuple[dict[str, int], list[int]]:
    return {
        'a': int(lines[0].split()[-1]),
        'b': int(lines[1].split()[-1]),
        'c': int(lines[2].split()[-1]),
    }, list(map(int, lines[4].split()[1].split(',')))

def run_instruction(registers: dict[str, int], operations: list[int]) -> list[int]:
    outputs = []
    pointer = 0

    def combo_value(value: int) -> int:
        if 0 <= value <= 3:
            return value

        op = {4: 'a', 5: 'b', 6: 'c'}
        return registers[op[value]]

    while pointer < len(operations):
        instruction = operations[pointer]
        operand = operations[pointer + 1]

        steps = 2
        if instruction == 0:
            registers['a'] = registers['a'] // (2 ** combo_value(operand))

        elif instruction == 1:
            registers['b'] = registers['b'] ^ operand

        elif instruction == 2:
            registers['b'] = combo_value(operand) % 8

        elif instruction == 3:
            if registers['a'] != 0:
                pointer = operand
                continue

        elif instruction == 4:
            registers['b'] = registers['b'] ^ registers['c']

        elif instruction == 5:
            outputs.append(combo_value(operand) % 8)

        elif instruction == 6:
            registers['b'] = registers['a'] // (2 ** combo_value(operand))

        elif instruction == 7:
            registers['c'] = registers['a'] // (2 ** combo_value(operand))

        pointer += steps

    return outputs

def handle_part_1(lines: list[str]) -> str:
    registers, operations = get_registers_and_instructions(lines)

    return ','.join(map(str,run_instruction(registers, operations)))


def handle_part_2(lines: list[str]) -> int:
    registers, operations = get_registers_and_instructions(lines)
    registers['a'] = 1
    divisor = operations[operations.index(0)+1]

    for i in range(1, len(operations)+1):
        output = run_instruction({a:b for a,b in registers.items()}, operations)
        while output != operations[-i:]:
            registers['a'] += 1
            output = run_instruction({a: b for a, b in registers.items()}, operations)

        registers['a'] *= (2**divisor)

    return registers['a'] // 8
