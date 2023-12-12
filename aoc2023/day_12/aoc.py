def handle_part_1(lines: list[str]) -> int:
   total = 0
   for i, line in enumerate(lines):
       springs, conditions = line.split()
       conditions = tuple([int(n) for n in conditions.split(',')])
       total += get_nb_arrangements_rec(springs, conditions)
   return total


def handle_part_2(lines: list[str]) -> int:
   total = 0
   for i, line in enumerate(lines):
       springs, conditions = line.split()
       springs = "?".join([springs for _ in range(5)])
       conditions = ",".join([conditions for _ in range(5)])
       conditions = tuple([int(n) for n in conditions.split(',')])

       total += get_nb_arrangements_rec(springs, conditions)
   return total

cache = {}
def get_nb_arrangements_rec(springs, conditions):
    if (springs, conditions) in cache:
        return cache[(springs, conditions)]

    if conditions == ():
        return 1 if springs.count('#') == 0 else 0

    if springs == "":
        return 1 if conditions == () else 0

    nb = 0
    if springs[0] == '.' or springs[0] == '?':
        nb += get_nb_arrangements_rec(springs[1:], conditions)

    if springs[0] == '#' or springs[0] == '?':
        if len(springs) >= conditions[0] and springs[:conditions[0]].count('.') == 0 and (len(springs) == conditions[0] or springs[conditions[0]] != '#'):
            nb += get_nb_arrangements_rec(springs[conditions[0] + 1:], conditions[1:])

    cache[(springs, conditions)] = nb
    return nb