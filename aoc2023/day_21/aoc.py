from collections import deque
from python.libraries.array import inbound
from python.libraries.utils import directNeighbors

def handle_part_1(lines: list[str]) -> int:
    (start,) = [(r,c) for r, row in enumerate(lines) for c, col in enumerate(row) if col == 'S']
    return get_distances_for_steps(lines, start, 64)

def handle_part_2(lines: list[str]) -> int:
    lines = [[n for n in row] for row in lines]

    # we can use only one of the height or width as they are the same
    block_size = len(lines)
    ((start_r, start_c),) = [(r, c) for r, row in enumerate(lines) for c, col in enumerate(row) if col == 'S']

    # the limit and the size of a block are odd
    limit = 26501365

    # how many blocks do we need to go from the edge of the center to the far end in any direction in direct line
    # the limit minus the half of the size is a multiple of the size (limit = (limit // block_size) * block_size + block_size // 2)
    nb_blocks = (limit - block_size//2) // block_size

    # an odd block is a block for which the center (mirror of start position) is reached in (1 * size) * n (odd number of steps) which is fully reached
    # an event block is a block for which the center (mirror of start position) is reached in (2 * size) * n (even number of steps) which is fully reached
    nb_even_blocks = (nb_blocks - 1) ** 2
    nb_odd_blocks = nb_blocks ** 2

    # the odd points (the limit is odd & the size is odd as well) are reached
    # in an "odd" block after an event nb of steps from the center == start
    # in an "even" block after an odd nb of steps from the center == start
    nb_points_per_odd_block = get_distances_for_steps(lines, (start_r, start_c), block_size * 2)
    nb_points_per_even_block = get_distances_for_steps(lines, (start_r, start_c), (block_size * 2) + 1)

    # count the number of points reached in the blocks at the end of the direct line
    nb_points_end_top = get_distances_for_steps(lines, (block_size - 1, start_c), block_size - 1)
    nb_points_end_bottom = get_distances_for_steps(lines, (0, start_c), block_size - 1)
    nb_points_end_right = get_distances_for_steps(lines, (start_r, 0), block_size - 1)
    nb_points_end_left = get_distances_for_steps(lines, (start_r, block_size - 1), block_size - 1)

    # count the number of points reached in the blocks at the surroundings of the all reached blocks
    # 2 parts : a small part and a large part in the different blocks arounds
    # small part
    nb_points_surround_small_top_right = get_distances_for_steps(lines, (block_size - 1, 0), (block_size // 2) - 1)
    nb_points_surround_small_top_left = get_distances_for_steps(lines, (block_size - 1, block_size - 1), (block_size // 2) - 1)
    nb_points_surround_small_bottom_right = get_distances_for_steps(lines, (0, 0), (block_size // 2) - 1)
    nb_points_surround_small_bottom_left = get_distances_for_steps(lines, (0, block_size - 1), (block_size // 2) - 1)

    # large part
    nb_points_surround_large_top_right = get_distances_for_steps(lines, (block_size - 1, 0),  (3 * block_size // 2) - 1)
    nb_points_surround_large_top_left = get_distances_for_steps(lines, (block_size - 1, block_size - 1), (3 * block_size // 2) - 1)
    nb_points_surround_large_bottom_right = get_distances_for_steps(lines, (0, 0), (3 * block_size // 2) - 1)
    nb_points_surround_large_bottom_left = get_distances_for_steps(lines, (0, block_size - 1), (3 * block_size // 2) - 1)


    return (nb_points_per_odd_block * nb_odd_blocks +
            nb_points_per_even_block * nb_even_blocks +
            nb_points_end_top + nb_points_end_bottom + nb_points_end_left + nb_points_end_right +
            nb_blocks * (nb_points_surround_small_top_right + nb_points_surround_small_bottom_right + nb_points_surround_small_bottom_left + nb_points_surround_small_top_left) +
            (nb_blocks - 1) * (nb_points_surround_large_top_right + nb_points_surround_large_bottom_right + nb_points_surround_large_bottom_left + nb_points_surround_large_top_left))


def get_distances_for_steps(lines, start, steps):
    seen = set(start)
    to_visit = deque([(start, steps)])
    found = set() # must be a set to avoid counting twice the same landing points
    
    while to_visit:
        (r, c), s = to_visit.popleft()

        if s % 2 == 0:
            found.add((r,c))

        if s == 0:
            continue

        for (dr, dc) in directNeighbors:
            nr, nc = r + dr, c + dc
            if inbound(nr, nc, len(lines), len(lines[0])) and lines[nr][nc] != '#' and (nr, nc) not in seen:
                seen.add((nr, nc))
                to_visit.append(((nr, nc), s - 1))

    return len(found)