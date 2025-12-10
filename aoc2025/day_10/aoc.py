from collections import deque
from z3 import *

def handle_part_1(lines: list[str]) -> int:
    total = 0
    for line in lines:
        target, *actions, _ = line.split()
        target = tuple([0 if c == '.' else 1 for c in target[1:-1]])
        actions = [list(map(int, a[1:-1].split(','))) for a in actions]

        to_visit = deque([(tuple([0 for _ in range(len(target))]), 0)])
        visited = set()
        
        while to_visit:
            lights, steps = to_visit.popleft()

            if lights == target:
                total += steps
                break
            
            if lights in visited:
                continue

            for a in actions:
                to_visit.append((tuple([c if i not in a else 1 - c for i,c in enumerate(lights)]), steps + 1))

            visited.add(lights)

    return total

        

def handle_part_2(lines: list[str]) -> int:
    total = 0
    for line in lines:
        _, *actions, target = line.split()
        actions = [list(map(int, a[1:-1].split(','))) for a in actions]
        target = tuple(map(int,target[1:-1].split(',')))

        def compute(steps):
            joltage = [0 for _ in range(len(target))]
        
            for s, n in enumerate(steps):
                for x in actions[s]:
                    joltage[x] += n 
            return tuple(joltage)

        # if action 0 = (3) and action 1 = (1,3) and the target for the 4th item in the target is 7, then we have n_steps_action_0 + n_steps_action_1 = 7 stored ((0,1), 7)
        equations = [(tuple(action_idx for action_idx, action in enumerate(actions) if target_idx in action), value) for target_idx, value in enumerate(target)]
        # max number of steps for each action separately
        max_steps = tuple([min(target[x] for x in a) for a in actions])
        s_m_steps = sorted([(v,i) for i, v in enumerate(max_steps)])
        
        def is_valid(steps):
            for elems, m in equations:
                if sum(steps[i] for i in elems) > m: return False
            return True
        
        variables = [Int(f"x{i}") for i in range(len(actions))]
        solver = Optimize()
        for elems, m in equations:
            solver.add(m == sum([variables[i] for i in elems]))
        for m, i in s_m_steps:
            solver.add(0 <= variables[i])
            solver.add(variables[i] <= m)

        solver.minimize(sum(variables))
        solver.check()
        model = solver.model()
        total += sum([model[i].as_long() for i in variables])


    return total
