
def handle_part_1(lines: list[str]) -> int:
    return "".join(dance(list('abcdefghijklmnop'), lines[0].split(',')))


def handle_part_2(lines: list[str]) -> int:
    programs = list('abcdefghijklmnop')
    actions = lines[0].split(',')
    dances = []
    dance_set = set()

    i=0
    target = 1000000000
    found = False
    while i < target:
        id = "".join(programs)
        if id in dance_set and not found:
            i = i* (target//i)
            found = True
        dances.append(id)
        dance_set.add(id)

        next = dance(programs, actions)
        programs = next
        i+=1
    return "".join(programs)

def dance(programs: list[str], actions: list[str]):
    for action in actions:
        if action[0] == 's':
            d = -1 * int(action[1:])
            programs = programs[d:] + programs[:d]

        elif action[0] == 'x':
            a,b = list(map(int, action[1:].split('/')))
            temp = programs[a]
            programs[a] = programs[b]
            programs[b] = temp

        elif action[0] == 'p':
            one,two = action[1:].split('/')

            iOne = programs.index(one)
            iTwo = programs.index(two)
            temp = programs[iOne]
            programs[iOne] = programs[iTwo]
            programs[iTwo] = temp

    return programs
