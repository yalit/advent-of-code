from functools import cmp_to_key


def handle_part_1(lines: list[str]) -> int:
    rules = {}
    empty_index = lines.index("")
    for line in lines[:empty_index]:
        x,y = line.split('|')
        if y not in rules:
            rules[y] = set()
        rules[y].add(x)

    total = 0
    for line in lines[empty_index+1:]:
        pages = line.split(',')
        if all(p not in rules or pp in rules[p] for i, p in enumerate(pages) for pp in pages[:i]) and all(p not in rules or pp not in rules[p] for i, p in enumerate(pages) for pp in pages[i+1:]):
            total += int(pages[len(pages)//2])
    return total


def handle_part_2(lines: list[str]) -> int:
    rules = {}
    empty_index = lines.index("")
    for line in lines[:empty_index]:
        x,y = line.split('|')
        if y not in rules:
            rules[y] = set()
        rules[y].add(x)


    def sort_pages(a, b):
        if a in rules and b in rules[a]:
            return 1
        return -1
            
    total = 0
    for line in lines[empty_index+1:]:
        pages = line.split(',')
        if all(p not in rules or pp in rules[p] for i, p in enumerate(pages) for pp in pages[:i]) and all(p not in rules or pp not in rules[p] for i, p in enumerate(pages) for pp in pages[i+1:]):
            continue
        total += int(sorted(pages, key=cmp_to_key(sort_pages))[len(pages)//2])
    return total
