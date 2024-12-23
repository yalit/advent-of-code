def handle_part_1(lines: list[str]) -> int:
    graph = {}
    for line in lines:
        parts = line.split("-")
        if parts[0] not in graph:
            graph[parts[0]] = []
        if parts[1] not in graph:
            graph[parts[1]] = []
        graph[parts[0]].append(parts[1])
        graph[parts[1]].append(parts[0])

    connections = {}

    for node in graph:
        for i, n in enumerate(graph[node]):
            for m in graph[node][i:]:
                trio = tuple(sorted([node, n, m]))
                if not (any(x.startswith('t') for x in trio)):
                    continue
                if trio not in connections:
                    connections[trio] = 0
                connections[trio] += 1

    return len([n for n, c in connections.items() if c == 3])

def combinations(lst: list[str], n: int) -> list[tuple[str]]:
    if n == 0:
        return []
    if n == 1:
        return [(x,) for x in lst]
    res = []
    for i, x in enumerate(lst):
        for comb in combinations(lst[i+1:], n - 1):
            res.append(tuple(sorted((x,) + comb)))
    return res

def handle_part_2(lines: list[str]) -> str:
    graph = {}
    for line in lines:
        parts = line.split("-")
        if parts[0] not in graph:
            graph[parts[0]] = ()
        if parts[1] not in graph:
            graph[parts[1]] = ()
        graph[parts[0]] = graph[parts[0]] + (parts[1],)
        graph[parts[1]] = graph[parts[1]] + (parts[0],)

    largest = max(len(graph[n]) + 1 for n in graph)
    found = None
    while not found:
        computer_sets = {}
        for n, edges in graph.items():
            combs = combinations(list((n,)+edges), largest)
            for comb in combs:
                if comb not in computer_sets:
                    computer_sets[comb] = 0
                computer_sets[comb] += 1
                if computer_sets[comb] == largest:
                    found = comb
                    break
            if found:
                break
        largest -= 1
    return ','.join(sorted(found))

