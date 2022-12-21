import sympy


def operation(registry, current):
    reg = registry[current]
    if len(reg) == 1:
        return int(reg[0])

    return eval(f"{operation(registry, reg[0])}{reg[1]}{operation(registry, reg[2])}")


def operationPart2(registry, current):
    reg = registry[current]
    if current == 'humn':
        return 'x'

    if len(reg) == 1:
        return reg[0]

    return f'({operationPart2(registry, reg[0])} {reg[1]} {operationPart2(registry, reg[2])})'


def handle_part_1(lines: list[str]) -> int:
    registry = {line.split(":")[0]: line.split(': ')[1].split() for line in lines}
    return operation(registry, 'root')


def handle_part_2(lines: list[str]) -> int:
    registry = {line.split(":")[0]: line.split(': ')[1].split() for line in lines}
    left, _, right = registry['root']

    doesNeedHuman = False
    next = [left]
    while next and not doesNeedHuman:
        elem = next.pop()
        if elem == 'humn':
            doesNeedHuman = True
            continue
        if len(registry[elem]) > 1:
            next.append(registry[elem][0])
            next.append(registry[elem][2])
    known = right if doesNeedHuman else left

    total = operation(registry, known)
    registry[known] = [total]
    registry['root'] = [left, '-', right]

    x = sympy.symbols('x')
    return sympy.solve(operationPart2(registry, 'root'), x)
