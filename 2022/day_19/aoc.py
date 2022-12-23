import re


def dfs(blueprint, maxResourcesNeeded, cache, minutes, robots, resources):
    if minutes == 0:
        return resources[3]

    cache_key = tuple([minutes, *robots, *resources])
    if cache_key in cache:
        return cache[cache_key]

    maxGeodes = resources[3] + (robots[3] * minutes)

    for r, bp in enumerate(blueprint):
        if r != 3 and robots[r] >= maxResourcesNeeded[r]:
            continue

        nb_turns = 0
        for r_needed, r_type in bp:
            if robots[r_type] == 0:
                break
            nb_turns = max(nb_turns, -(-(r_needed - resources[r_type]) // robots[r_type]))
        else: # only if for loop didn't break
            remaining_time = minutes - nb_turns - 1
            if remaining_time <= 0:
                continue

            n_resources = [a + (b * (nb_turns + 1)) for a, b in zip(resources, robots)]
            n_robots = robots[:]
            n_robots[r] += 1
            for r_needed, r_type in bp:
                n_resources[r_type] -= r_needed
            for i, m in enumerate(maxResourcesNeeded):
                n_resources[i] = min(m * remaining_time, n_resources[i])
            maxGeodes = max(maxGeodes, dfs(blueprint, maxResourcesNeeded, cache, remaining_time, n_robots, n_resources))

    cache[cache_key] = maxGeodes
    return maxGeodes


def handle_part_1(lines: list[str]) -> int:
    maxResourcesNeeded = [0, 0, 0]
    s = 0
    for k, line in enumerate(lines):
        robots = line.split('.')
        blueprint = []
        for robot in robots[:-1]:
            # ore / clay / obsidian
            nb_items_needed = []
            for n, r in re.findall(r'(\d+) (\w+)', robot):
                i = ['ore', 'clay','obsidian'].index(r)
                nb_items_needed.append((int(n), i))
                maxResourcesNeeded[i] = max(maxResourcesNeeded[i], int(n))
            blueprint.append(nb_items_needed)
        print(blueprint)

        # ore / clay / obsidian / geodes (same for robot)
        m = dfs(blueprint, maxResourcesNeeded, {}, 24, [1, 0, 0, 0], [0, 0, 0, 0])
        print(k + 1, blueprint, m)
        s += (k + 1) * m

    return s


def handle_part_2(lines: list[str]) -> int:
    return 0
