from python.libraries.utils import lcm

direction = {'L': 0, 'R': 1}

def handle_part_1(lines: list[str]) -> int:
    pattern = lines[0]
    nodes = {line.split(' = ')[0]: line.split(' = ')[1][1:-1].split(', ') for  line in lines[2:]}

    current_node = 'AAA'
    step = 0
    while current_node != 'ZZZ':
        current_node = get_next_node(nodes, pattern, current_node,step)
        step += 1


    return step


def handle_part_2(lines: list[str]) -> int:
    pattern = lines[0]
    nodes = {line.split(' = ')[0]: line.split(' = ')[1][1:-1].split(', ') for line in lines[2:]}

    a_nodes = [node for node in nodes.keys() if node[-1] == 'A']
    nb_steps_z_for_a = [get_nb_step_until_next_z(nodes, pattern, node, 0) for node in a_nodes]
    # nb_steps_z_for_z = [get_nb_step_until_next_z(nodes, pattern, node[1], node[0]) for node in nb_steps_z_for_a]
    # the just above calculation is to check from the Z nodes you land on for each of the A nodes, where do you arrive while continuing
    # after verification, both arrays above are the same and so, there is a loop starting from 1 start A node, you arrive to a Z node
    # and from that Z node, it takes the same amount of step to come back to the same Z node
    # we can also verify that the nb_steps of each loop is a multiple of the length of the LR "pattern" with
    # print(all([True if node[0] % len(pattern) == 0 else False for node in nb_steps_z_for_a]))
    # so you can just take the lcm (least common multiple) of every nb steps of nb_steps_z_for_a as it's a loop for every node
    return lcm(*[x[0] for x in nb_steps_z_for_a])

def get_nb_step_until_next_z(nodes, pattern, start_node, start_step):
    c_node = get_next_node(nodes, pattern, start_node, 0)
    step = start_step + 1
    while not c_node[-1] == 'Z':
        c_node = get_next_node(nodes, pattern, c_node, step)
        step += 1

    return [step - start_step, c_node]

def get_next_node(nodes, pattern, node, step):
    return nodes[node][direction[pattern[step % len(pattern)]]]


