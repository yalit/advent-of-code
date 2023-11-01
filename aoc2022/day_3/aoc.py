import string

alphabet = string.ascii_lowercase + string.ascii_uppercase


def handle_part_1(lines: list[str]) -> int:
    def filterItem(item: str) -> int:
        [first, second] = [item[0:int(len(item) / 2)], item[int(len(item) / 2):]]
        return sum(list(map(lambda x: alphabet.find(x) + 1, list(set(filter(lambda x: x in second, first))))))

    return sum(list(map(filterItem, lines)))


def handle_part_2(lines: list[str]) -> int:
    return sum(list(map(lambda x: alphabet.find(x) + 1, [list(set(filter(lambda l1: l1 in lines[i], filter(lambda l2: l2 in lines[i+1], lines[i+2]))))[0] for i in range(0, len(lines)-1, 3)])))

