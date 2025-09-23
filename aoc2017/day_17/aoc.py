from collections import deque 

def handle_part_1(lines: list[str]) -> int:
    buffer = [0]
    pos = 0
    steps = int(lines[0])
        
    for i in range(1, 2018):
        pos = ((pos + steps) % i)+1
        buffer = buffer[:pos] + [i] + buffer[pos:]

    return buffer[(pos+1)%len(buffer)]


def handle_part_2(lines: list[str]) -> int:
    delta = int(lines[0])
    spinlock = deque([0])

    for i in range(1, 50000001):
        spinlock.rotate(-delta)
        spinlock.append(i)

    return spinlock[spinlock.index(0) + 1]
        
