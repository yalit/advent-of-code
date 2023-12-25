import networkx as nx
import matplotlib.pyplot as plt

def handle_part_1(lines: list[str]) -> int:
    g = nx.Graph()
    graph = {}
    for line in lines:
        f, to = line.split(': ')
        if f not in graph:
            graph[f] = set()
            g.add_node(f)

        for n in to.split():
            if n not in graph:
                graph[n] = set()
                g.add_node(n)
            graph[f].add(n)
            g.add_edge(f, n)
            graph[n].add(f)

    cuts = nx.minimum_edge_cut(g)
    for f,t in cuts:
        graph[f].remove(t)
        graph[t].remove(f)

    to_visit = [list(graph.keys())[0]]
    seen = set()
    while to_visit:
        n = to_visit.pop()
        seen.add(n)
        for neighbor in graph[n]:
            if neighbor not in seen:
                to_visit.append(neighbor)

    return (len(graph.keys()) - len(seen)) * len(seen)


def handle_part_2(lines: list[str]) -> int:
    return 0
