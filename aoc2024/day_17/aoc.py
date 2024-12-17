def get_registers_and_instructions(lines: list[str]) -> tuple[dict[str, int], list[int]]:
    return {
        'a': int(lines[0].split()[-1]),
        'b': int(lines[1].split()[-1]),
        'c': int(lines[2].split()[-1]),
    }, list(map(int, lines[4].split()[1].split(',')))

def xor(a: int, b: int) -> int:
    return a ^ b

def run_instruction(registers: dict[str, int], operations: list[int]) -> list[int]:
    outputs = []
    pointer = 0

    def get_operand_value(combo: bool) -> int:
        operand = operations[pointer + 1]

        if not combo or 0 <= operand <= 3:
            return operand

        op = {4: 'a', 5: 'b', 6: 'c'}
        return registers[op[operand]]

    while pointer < len(operations):
        instruction = operations[pointer]

        steps = 2
        if instruction == 0:
            registers['a'] = registers['a'] // (2 ** get_operand_value(True))

        elif instruction == 1:
            registers['b'] = xor(registers['b'], get_operand_value(False))

        elif instruction == 2:
            registers['b'] = get_operand_value(True) % 8

        elif instruction == 3:
            if registers['a'] != 0:
                pointer = get_operand_value(False)
                continue

        elif instruction == 4:
            registers['b'] = xor(registers['b'], registers['c'])

        elif instruction == 5:
            outputs.append(get_operand_value(True) % 8)

        elif instruction == 6:
            registers['b'] = registers['a'] // (2 ** get_operand_value(True))

        elif instruction == 7:
            registers['c'] = registers['a'] // (2 ** get_operand_value(True))

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
