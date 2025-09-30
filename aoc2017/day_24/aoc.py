def handle_part_1(lines: list[str]) -> int:
    components = [tuple(map(int, line.split("/"))) for line in lines]

    to_visit = [(c, c[1] if c[0] == 0 else c[0], []) for c in components if 0 in c]

    max_strength = 0
    while to_visit:
        current, next_link, chain = to_visit.pop()
        chain = chain + [current]

        possible_chained_components = [c for c in components if c not in chain and next_link in c]

        if len(possible_chained_components) == 0:
            strength = sum(sum(c) for c in chain)
            max_strength = max(max_strength, strength)
            continue

        for c in possible_chained_components:
            to_visit.append((c, c[1] if c[0] == next_link else c[0], chain))

    return max_strength


def handle_part_2(lines: list[str]) -> int:
    components = [tuple(map(int, line.split("/"))) for line in lines]

    to_visit = [(c, c[1] if c[0] == 0 else c[0], []) for c in components if 0 in c]

    longest_chain = []
    while to_visit:
        current, next_link, chain = to_visit.pop()
        chain = chain + [current]

        possible_chained_components = [c for c in components if c not in chain and next_link in c]

        if len(possible_chained_components) == 0:
            if len(chain) > len(longest_chain):
                longest_chain = chain
            elif len(chain) == len(longest_chain):
                if sum(sum(c) for c in chain) > sum(sum(c) for c in longest_chain):
                    longest_chain = chain
            continue

        for c in possible_chained_components:
            to_visit.append((c, c[1] if c[0] == next_link else c[0], chain))

    return sum(sum(c) for c in longest_chain)
