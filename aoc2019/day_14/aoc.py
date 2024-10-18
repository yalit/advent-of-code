from math import ceil


def handle_part_1(lines: list[str]) -> int:
    reactions = {}
    for line in lines:
        inputs, output = line.split(" => ")
        output_amount, output_name = output.split(" ")
        inputs = inputs.split(", ")
        reactions[output_name] = (int(output_amount), [(int(i.split(" ")[0]), i.split(" ")[1]) for i in inputs])

    ore  = 0
    components = [(1, "FUEL")]
    leftovers = {}

    while components:
        need, component = components.pop(0)
        if component == "ORE":
            ore += need
            continue

        if component not in leftovers:
            leftovers[component] = 0
        if leftovers[component] >= need:
            leftovers[component] -= need
            continue
        else:
            need -= leftovers[component]
            leftovers[component] = 0
        amount, inputs = reactions[component]
        multiplier = ceil(need / amount) # nb of time the reaction has to be done
        leftovers[component] += (amount * multiplier) - need

        for n, c in inputs:
            input_needed = n * multiplier
            components.append((input_needed, c))

    return ore


def handle_part_2(lines: list[str]) -> int:
    reactions = {}
    for line in lines:
        inputs, output = line.split(" => ")
        output_amount, output_name = output.split(" ")
        inputs = inputs.split(", ")
        reactions[output_name] = (int(output_amount), [(int(i.split(" ")[0]), i.split(" ")[1]) for i in inputs])

    ore  = 0
    limit = 1000000000000
    fuel = -1
    leftovers = {}
    needs = {}
    for k in reactions:
        print(k, reactions[k])
    while ore < limit:
        components = [(1, "FUEL")]
        fuel += 1
        while components:
            need, component = components.pop(0)
            if component == "ORE":
                ore += need
                continue

            if component not in leftovers:
                leftovers[component] = 0
            if leftovers[component] >= need:
                leftovers[component] -= need
                continue
            else:
                need -= leftovers[component]
                leftovers[component] = 0
            amount, inputs = reactions[component]
            multiplier = ceil(need / amount)  # nb of time the reaction has to be done
            leftovers[component] += (amount * multiplier) - need

            for n, c in inputs:
                input_needed = n * multiplier
                components.append((input_needed, c))
                if c not in needs:
                    needs[c] = 0
                needs[c] += input_needed

    return fuel