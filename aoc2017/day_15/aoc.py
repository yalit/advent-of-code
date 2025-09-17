from collections import deque

def handle_part_1(lines: list[str]) -> int:
    valueA = int(lines[0].split()[-1])
    valueB = int(lines[1].split()[-1])
    factorA = 16807
    factorB = 48271

    total = 0
    for _ in range(40000000):
        valueA = next_value(valueA, factorA)
        valueB = next_value(valueB, factorB)
        
        if bin(valueA)[-16:] == bin(valueB)[-16:]:
            total += 1

    return total 


def handle_part_2(lines: list[str]) -> int:
    valueA = int(lines[0].split()[-1])
    valueB = int(lines[1].split()[-1])
    factorA = 16807
    factorB = 48271

    total = 0
    valuesA = deque([])
    valuesB = deque([])
    compared = 0
    while compared < 5000000:
        valueA = next_value(valueA, factorA)
        valueB = next_value(valueB, factorB)
        
        if valueA % 4 == 0:
            valuesA.append(valueA)

        if valueB % 8 == 0:
            valuesB.append(valueB)

        if len(valuesA) > 0 and len(valuesB) > 0:
            compared += 1
            a = valuesA.popleft()
            b = valuesB.popleft()
            if bin(a)[-16:] == bin(b)[-16:]:
                total += 1

    return total 

def next_value(value, factor):
    return (value*factor) % 2147483647
