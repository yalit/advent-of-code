def handle_part_1(lines: list[str]) -> int:
    nodes = {}

    for line in lines[2:]:
        while line.count("  ") > 0:
            line = line.replace("  ", " ")

        node, size, used, available, _ = line.split(" ")
        _, x, y = node.split("-")
        nodes[(int(x[1:]), int(y[1:]))] = (
            int(size[:-1]),
            int(used[:-1]),
            int(available[:-1]),
        )

    viable_pairs = 0
    for i, node in enumerate(nodes.items()):
        for j, other_node in enumerate(nodes.items()):
            if j == i:
                continue

            # one side
            # node in the form of((x,y), (size, used, available))
            viable_pairs += (
                1 if node[1][1] > 0 and node[1][1] <= other_node[1][2] else 0
            )

    return viable_pairs


def handle_part_2(lines: list[str]) -> int:
    nodes = {}

    for line in lines[2:]:
        while line.count("  ") > 0:
            line = line.replace("  ", " ")

        node, size, used, available, _ = line.split(" ")
        _, x, y = node.split("-")
        nodes[(int(x[1:]), int(y[1:]))] = (
            int(size[:-1]),
            int(used[:-1]),
            int(available[:-1]),
        )

    max_x = max([x for x, _ in nodes])
    max_y = max([y for _, y in nodes])
    d = []
    for y in range(max_y + 1):
        d.append([])
        for x in range(max_x + 1):
            d[y].append(f"{nodes[(x,y)][1]}/{nodes[(x,y)][0]}")

    for r in d:
        print("".join(["{:<8}".format(x) for x in r]))

    # looked at the display and counter the number of steps
    # X (34) to move the empty spot near the start of the data and moving the data to it
    # + Y (4) moves to move the blank space around and move the target data * 35 the number of times to repeat to move it to the target place
    return 209
