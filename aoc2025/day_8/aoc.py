import math
from functools import reduce

def d(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def handle_part_1(lines: list[str]) -> int:
    dist = {}
    boxes = [tuple(map(int, line.split(','))) for line in lines]
    junctions ={x: set() for x in boxes} 
    
    for i, a in enumerate(boxes):
        for b in boxes[i+1:]:
            distance = d(a,b)
            dist[distance] = (a,b)

    keys = sorted(dist.keys())
    i = 0
    m = 10
    while i < m:
        distance = min(dist.keys())
        a,b = dist[distance]
        del dist[distance]

        junctions[a].add(b)
        junctions[b].add(a)
        i+=1


    circuits = []
    visited = set()
    boxes = set(boxes)

    while boxes:
        c = set()
        to_visit = [boxes.pop()]
        while to_visit:
            box = to_visit.pop()
            
            if box in c:
                continue

            for b in junctions[box]:
                to_visit.append(b)

            visited.add(box)
            c.add(box)


        circuits.append(c)        
        boxes -= c
    return reduce(lambda t,n: t*len(n), (sorted(circuits, key=lambda x: len(x), reverse=True)[:3]), 1)

def handle_part_2(lines: list[str]) -> int:
    dist = {}
    boxes = [tuple(map(int, line.split(','))) for line in lines]
    
    for i, a in enumerate(boxes):
        for b in boxes[i+1:]:
            distance = d(a,b)
            dist[distance] = (a,b)


    circuits = []
    keys = sorted(dist.keys(), reverse=True)
    distance = keys.pop()
    circuits.append(set(dist[distance]))

    while keys:
        distance = keys.pop()
        a,b = dist[distance]


        matched = {a: None, b: None}
        for i, c in enumerate(circuits):
            if a in c:
                matched[a] = i
            if b in c:
                matched[b] = i
            if all(x is not None for x in matched.values()):
                break

        if all(x is None for x in matched.values()):
            circuits.append(set([a,b]))
        elif all(x is not None for x in matched.values()):
            if matched[a] != matched[b]:
                # present in different circuits so join the circuits
                mi = min(x for x in matched.values())
                ma = max(x for x in matched.values())
                c_a = circuits.pop(mi)
                c_b = circuits.pop(ma -1)
                circuits.append(c_a | c_b)
        else:
            # at least one is None so join the other to the same circuit
            if matched[a] is None:
                circuits[matched[b]].add(a)
            else:
                circuits[matched[a]].add(b)

        if len(circuits) > 0 and len(circuits[0]) == len(lines):
            print(a, b)
            return a[0] * b[0]

    return None

