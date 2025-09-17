def handle_part_1(lines: list[str]) -> int:
    line = lines[0] + lines[0][0]
    sum = 0

    for c in range (len(line)-1):
        n = (c+1) % len(line)
        if line[c] == line[n]:
            sum += int(line[c])
    return sum

def handle_part_2(lines: list[str]) -> int:
    line = lines[0]
    sum = 0
    delta = len(line)//2
    
    for c in range (len(line)-1):
        n = (c+delta) % len(line)
        if line[c] == line[n]:
            sum += int(line[c])
    return sum
