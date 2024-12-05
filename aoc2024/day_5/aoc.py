from functools import cmp_to_key

def is_page_valid(rules, pages):
    for i, page in enumerate(pages):
        #check before
        for p_page in pages[:i]:
            if page in rules and p_page not in rules[page]:
                return False
        
        # check after
        for p_page in pages[i+1:]:
            if page in rules and p_page in rules[page]:
                return False
    return True

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
        if is_page_valid(rules, pages):
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
        if not is_page_valid(rules, pages):
            total += int(sorted(pages, key=cmp_to_key(sort_pages))[len(pages)//2])
    return total
