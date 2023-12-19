import functools
import re


def handle_part_1(lines: list[str]) -> int:
    workflows, parts_list = get_workflows_and_parts(lines)


    total = 0
    for parts in parts_list:
        if check_part(workflows, parts) == 'A':
            total += sum(parts.values())


    return total


def handle_part_2(lines: list[str]) -> int:
    workflows, _ = get_workflows_and_parts(lines)

    inverse = {'<': '>', '>': '<'}
    a_paths = []

    to_visit = [('in', 0, None, ())] #conditions will be (([xmas], [<>], nb)

    while to_visit:
        wf, step, result, conditions = to_visit.pop()
        if result == 'A':
            a_paths.append(conditions)
            continue
        elif result == 'R':
            continue

        rule = workflows[wf][step]

        if ':' not in rule:
            to_visit.append((rule, 0, rule, conditions))
            continue

        p, operation, limit, result = re.match(r'([xmas])([<>])(\d+):([A-Za-z]+)', rule).groups()

        #matching criteria
        to_visit.append((result, 0, result, conditions + ((p, operation, int(limit)),)))

        #not matching criteria
        to_visit.append((wf, step + 1, None, conditions+ ((p, inverse[operation], (int(limit) + 1 if operation == '>' else int(limit) - 1)),)))

    combinations = 0
    for path in a_paths:
        mm = {k: (1,4000) for k in ['x','m','a','s']}
        for p, operation, limit in path:
            if operation == '<':
                mm[p] = (mm[p][0], min(limit - 1, mm[p][1]))
            elif operation == '>':
                mm[p] = (max(limit + 1, mm[p][0]), mm[p][1])

        combinations += functools.reduce(lambda t,n: t * n, [e[1] - e[0] + 1 for e in mm.values()], 1)

    return combinations


def get_workflows_and_parts(lines):
    workflows = {}
    parts = []

    # get
    for line in lines:
        if len(line) == 0:
            continue
        #treat workflows
        if line[0] != '{':
            wf, instructions = line.replace('}', "").split("{")
            workflows[wf] = instructions.split(',')

        #treat parts
        else:
            elements = line.replace('{','').replace('}','')
            parts.append({k: int(v) for k,v in [e.split('=') for e in elements.split(',')]})


    return workflows, parts

def check_rule(rule, parts):
    if ':' not in rule:
        return rule

    p, operation, limit, result = re.match(r'([xmas])([<>])(\d+):([A-Za-z]+)',rule).groups()
    if operation == '<':
        if parts[p] < int(limit):
            return result
    elif operation == '>':
        if parts[p] > int(limit):
            return result

    return None

def check_part(workflows, parts):
    wf = 'in'
    rule = 0
    result = check_rule(workflows[wf][rule], parts)
    while result not in ['A', 'R']:
        if result is None:
            rule += 1
        else:
            wf = result
            rule = 0
        result = check_rule(workflows[wf][rule], parts)

    return result