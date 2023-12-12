import re

def handle_part_1(lines: list[str]) -> int:
   total = 0
   for line in lines[-1:]:
       add = get_nb_assignments(*line.split())
       print("line nb : ", add)
       total += get_nb_assignments(*line.split())
   return total


def handle_part_2(lines: list[str]) -> int:
    return 0

def get_nb_assignments(springs, conditions):
    nb = 0

    to_test = [(0, [x for x in springs.split('.') if len(x) > 0], [int(n) for n in conditions.split(',')])]
    
    while to_test:
        cur_step, spring, condition = to_test.pop()
        print(cur_step, spring, condition, nb)
        if len(condition) == 0:
            if len(spring) == 0:
                nb += 1
            continue
        if len(spring) == 0:
            continue
        
        s = spring[0]
        c = condition[0]

        if len(s) < c:
            print("spring not long enough")
            to_test.append((0,spring[1:], condition))
            continue

        if all([x == '#' for x in s[:c]]):
            if len(s) == c:
                print("found a full spring")
                to_test.append((0,spring[1:], condition[1:]))
            elif s[c] != '#':
                print("found a part of a spring")
                to_test.append((0,[s[c+1:]] + spring[1:], condition[1:]))
            continue

        if s[cur_step] == '#':
            print("testing the next part of the spring")
            to_test.append((cur_step+1, spring, condition))
            continue

        # can only use . on the first step if not finished
        if cur_step == 0 and len(s) > c:
            print("beginning of the spring, testing a '.'")
            to_test.append((0, [s[cur_step+1:]] + spring[1:], condition))
        
        # test '#'
        print("testing a '#'")
        s = s[:cur_step] + '#' + s[cur_step+1:]
        to_test.append((cur_step+1, [s]+spring[1:], condition))
        
    
    return nb