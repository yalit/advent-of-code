def is_possible(towels: set[str], max_size: int, pattern: str)-> bool:
    if pattern == "":
        return True

    for i in range(1, max_size+1):
        if pattern[-i:] in towels:
            if is_possible(towels, max_size, pattern[:-i]):
                return True

    return False

def handle_part_1(lines: list[str]) -> int:
    towels = set(sorted(lines[0].split(', ')))
    max_size = max(map(len, towels))

    count = 0
    for pattern in lines[2:]:
        count += 1 if is_possible(towels, max_size, pattern) else 0

    return count

def handle_part_2(lines: list[str]) -> int:
    towels = set(sorted(lines[0].split(', ')))
    max_size = max(map(len, towels))

    count = 0

    memoization = {}

    def is_possible_all(pattern: str, used:tuple[str] = ()) -> int:
        if pattern == "":
            return 1

        if pattern in memoization:
            return memoization[pattern]

        possible_combinations = 0
        for i in range(1, max_size + 1):
            if i <= len(pattern) and pattern[-i:] in towels:
                possible_combinations += is_possible_all(pattern[:-i], (pattern[-i:],) + used)

        memoization[pattern] = possible_combinations
        return possible_combinations


    for target in lines[2:]:
        memoization = {}
        count += is_possible_all(target)
    return count
