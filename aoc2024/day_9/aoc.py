import time

def handle_part_1(lines: list[str]) -> int:
    disk = []
    id = 0
    for i,x in enumerate(lines[0]):
        if i%2==0:
            disk += [id]*int(x)
            id +=1
        else:
            disk += [-1]*int(x)

    i = 0
    while i < len(disk):
        while disk[-1] <0: disk.pop()
        if i >= len(disk): break
        if disk[i] <0:
            disk[i] = disk.pop()
        i+=1

    return sum(i*x for i,x in enumerate(disk))


def handle_part_2(lines: list[str]) -> int:
    files = {}
    blanks = []
    id = 0
    pos = 0
    for i, x in enumerate(lines[0]):
        if i % 2 == 0:
            files[id] = (pos, int(x))
            id += 1
        else:
            blanks.append((pos,int(x)))
        pos += int(x)

    while id > 0:
        id -=1
        pos, size = files[id]
        for i, (start, length) in enumerate(blanks):
            if start >= pos:
                blanks = blanks[:i]
                break
            if size <= length:
                files[id] = (start, size)
                if size == length:
                    blanks.pop(i)
                else:
                    blanks[i] = (start+size, length-size)
                break

    return sum(sum(i*x for x in range(start, start+size)) for i, (start, size) in files.items())
