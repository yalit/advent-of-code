from collections import Counter

def handle_part_1(lines: list[str]) -> int:
    disk = get_disk(lines)

    n = list(disk.keys())[0]

    while n in disk:
        n = disk[n][0]
    return n


def handle_part_2(lines: list[str]) -> int:
    disk = {}

    for l in lines:
        d = l.replace(",", "").replace('(','' "").replace(")", "").split()
        
        disk[d[0]] = (int(d[1]), d[3:])

    base = handle_part_1(lines)
    correct_weight = 0
    n = base
    
    incorrect = True

    while incorrect:
        if is_balanced(disk, n):
            incorrect = False
            continue
            
        w = {}
        for a in disk[n][1]:
            i = get_weight(disk, a)
            if i not in w:
                w[i] = []
            w[i].append(a)

        correct_weight = [x for x, a in w.items() if len(a) > 1][0]
        n = [a[0] for x, a in w.items() if len(a) == 1][0]
    
    return correct_weight - get_weight(disk, n) + disk[n][0]

def get_disk(lines):
    disk = {}

    for l in lines:
        d = l.replace(",", "").split()

        for a in d[3:]:
            if a not in disk:
                disk[a] = []
            disk[a].append(d[0])
    
    return disk

def get_weight(disk, n):
    w = disk[n][0]

    for a in disk[n][1]:
        w += get_weight(disk, a)

    return w

def is_balanced(disk, n):
    s = set()

    if len(disk[n][1]) == 0:
        return True

    for a in disk[n][1]:
        s.add(get_weight(disk, a))
    
    return len(s) == 1