def get_value(operations: dict[str: tuple[str, str, str]], gates: dict[str:int], gate: str) -> int:
    if gate in gates:
        return gates[gate]

    operator, gate1, gate2 = operations[gate]

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

        operations[target] = (operator,) + tuple(sorted([gate_1, gate_2]))

    return gates, operations


def handle_part_1(lines: list[str]) -> int:
    gates, operations = get_gates_and_operations(lines)
    return get_number_value(operations, gates, 'z')

def print_output_operation(operations: dict[str: tuple[str, str, str]], gates: dict[str:int], output: str, depth: int = 0) -> str:
    if output in gates:
        return "  "*depth + output

    else:
        operator, gate1, gate2 = operations[output]
        return f"{'  '*depth + output} => {operator}\n{print_output_operation(operations, gates, gate1, depth+1)}\n{print_output_operation(operations, gates, gate2, depth+1)}"

def swap_operations(operations: dict[str: tuple[str, str, str]], a: str, b: str) -> dict[str: tuple[str, str, str]]:
    new_operations = {k:v for k,v in operations.items()}
    new_operations[a] = operations[b]
    new_operations[b] = operations[a]
    return new_operations




def handle_part_2(lines: list[str]) -> str:
    gates, operations = get_gates_and_operations(lines)
    x= get_gates_number_value(gates, 'x')
    y = get_gates_number_value(gates, 'y')

    # this swap is done manually by running the code below and inspecting each time there was an error ... :D
    swapped = ['z09', 'hnd', 'z16', 'tdv', 'z23', 'bks', 'nrn', 'tjp']
    operations = swap_operations(operations, 'z09', 'hnd')
    operations = swap_operations(operations, 'z16', 'tdv')
    operations = swap_operations(operations, 'z23', 'bks')
    operations = swap_operations(operations, 'tjp', 'nrn')
    target_operations = {}
    correspondences = {}
    errors = []

    def find_operation(operation: tuple[str, str, str]) -> str:
        print(f"Operation: {operation}")
        return [k for k, op in operations.items() if op == operation or op == (operation[0], operation[2], operation[1])][0]

    def n(s: str, i: int) -> str:
        return f"{s}{i:02}"

    for i in range(45):
        zi = n("z", i)
        xi = n("x", i)
        yi = n("y", i)
        ri = n("r", i)
        ii = n("i", i)
        iiminus = n("i", i-1)
        ai = n("a", i)
        oi = n("o", i)
        # ri = xi XOR yi
        target_operations[ri] = ('XOR', xi, yi)
        correspondences[ri] = find_operation(('XOR', xi, yi))
        # ai = xi AND yi
        target_operations[ai] = ('AND', xi, yi)
        correspondences[ai] = find_operation(('AND', xi, yi))
        if i == 0:
            # z0 = x0 XOR y0
            target_operations[f"z00"] = ('XOR', f"x00", f"y00")
            correspondences[f"z00"] = find_operation(('XOR', f"x00", f"y00"))
            # i0 = x0 AND y0
            target_operations[f"i00"] = target_operations[f"a00"]
            correspondences[f"i00"] = correspondences[f"a00"]
        else:
            # i1 = a1 OR (r1 AND i0) = a1 OR o1 (= r1 AND i0)
            target_operations[oi] = ('AND', ri, iiminus)
            correspondences[oi] = find_operation(('AND', correspondences[ri], correspondences[iiminus]))
            target_operations[ii] = ('OR', ai, oi)
            correspondences[ii] = find_operation(('OR', correspondences[ai], correspondences[oi]))


    return ",".join(sorted(swapped))
