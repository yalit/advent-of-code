def get_value(operations: dict[str: tuple[str, str, str]], gates: dict[str:int], gate: str) -> int:
    if gate in gates:
        return gates[gate]

    gate1, operator, gate2 = operations[gate]

    if operator == 'AND':
        return get_value(operations, gates, gate1) and get_value(operations, gates, gate2)
    elif operator == 'OR':
        return get_value(operations, gates, gate1) or get_value(operations, gates, gate2)
    elif operator == 'XOR':
        return get_value(operations, gates, gate1) ^ get_value(operations, gates, gate2)


def get_number_value(operations: dict[str: tuple[str, str, str]], gates: dict[str:int], g: str) -> int:
    values = list(reversed([get_value(operations, gates, gate) for gate in sorted(operations) if gate.startswith(g)]))
    return int(''.join(list(map(str, values))), 2)


def get_gates_number_value(gates: dict[str:int], g: str) -> int:
    return int(''.join(list(map(str, [gates[gate] for gate in sorted(gates) if gate.startswith(g)]))), 2)


def get_gates_and_operations(lines: list[str]):
    gates = {}
    i = 0
    while lines[i] != '':
        gate, value = lines[i].split(': ')
        gates[gate] = int(value)
        i += 1

    operations = {}
    for line in lines[i + 1:]:
        gate_1, operator, gate_2, _, target = line.split()

        operations[target] = (gate_1, operator, gate_2)

    return gates, operations


def handle_part_1(lines: list[str]) -> int:
    gates, operations = get_gates_and_operations(lines)
    return get_number_value(operations, gates, 'z')

def print_output_operation(operations: dict[str: tuple[str, str, str]], gates: dict[str:int], output: str, s: set[str]) -> set[str]:
    if output in gates:
        return s | {output}

    gate1, operator, gate2 = operations[output]
    return print_output_operation(operations, gates, gate1, s | {gate1}) | print_output_operation(operations, gates, gate2, s| {gate2})

def swap_operations(operations: dict[str: tuple[str, str, str]], a: str, b: str) -> dict[str: tuple[str, str, str]]:
    new_operations = {k:v for k,v in operations.items()}
    new_operations[a] = operations[b]
    new_operations[b] = operations[a]
    return new_operations

def handle_part_2(lines: list[str]) -> int:
    gates, operations = get_gates_and_operations(lines)
    x= get_gates_number_value(gates, 'x')
    y = get_gates_number_value(gates, 'y')
    target_z = bin(x+y)[2:]
    test_z = bin(get_number_value(operations, gates, 'z'))[2:]
    print(target_z, len(target_z))
    print(test_z, len(test_z))

    wrong_digits = []
    for i, c in enumerate(target_z):
        if c != test_z[i]:
            wrong_digits.append(i)
    print(wrong_digits)

    correct_digits = []
    for i, c in enumerate(target_z):
        if c == test_z[i]:
            correct_digits.append(i)
    print(correct_digits)

    same_for_wrong = set()
    for i in wrong_digits:
        z = f"z{45-i}" if 45-i >= 10 else f"z0{45-i}"
        same_for_wrong |= set([x for x in print_output_operation(operations, gates, z, set()) if not(x.startswith('x') or x.startswith('y'))])

    same_for_correct = set()
    for i in correct_digits:
        z = f"z{45 - i}" if 45 - i >= 10 else f"z0{45 - i}"
        same_for_correct |= set([x for x in print_output_operation(operations, gates, z, set()) if
                               not (x.startswith('x') or x.startswith('y'))])

    print(same_for_wrong - same_for_correct)

    return 0
