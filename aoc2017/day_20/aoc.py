def get_particules(lines: list[str]) -> list[tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]]:
    particules = []
    for i, line in enumerate(lines):
        p_str, v_str, a_str = line.split(", ")
        p = tuple(int(x) for x in p_str[3:-1].split(","))
        v = tuple(int(x) for x in v_str[3:-1].split(","))
        a = tuple(int(x) for x in a_str[3:-1].split(","))
        particules.append((i, p, v, a))
    return particules

def handle_part_1(lines: list[str]) -> int:
    particules = get_particules(lines)
    t = 1000000
    long_term_positions = [
        (p[0] + v[0] * t + a[0] * (t**2) / 2,
         p[1] + v[1] * t + a[1] * (t**2) / 2,
         p[2] + v[2] * t + a[2] * (t**2) / 2)
        for _, p, v, a in particules
    ]

    distances = [abs(x) + abs(y) + abs(z) for x, y, z in long_term_positions]

    return distances.index(min(distances))


def handle_part_2(lines: list[str]) -> int:
    parts = get_particules(lines)

    # compute the intersections of the particules
    collisions = set()

    for x in range(1, 1000):
        parts = [(i, (p[0] + v[0] + a[0], p[1] + v[1] + a[1], p[2] + v[2] + a[2]), (v[0] + a[0], v[1] + a[1], v[2] + a[2]),a,) for i, p, v, a in parts ]

        current_collisions = set()
        for i, (a, pa,_,_) in enumerate(parts):
            for j, (b, pb, _, _) in enumerate(parts[i+1:], start=i+1):
                if a in collisions or b in collisions:
                    continue
                if pa == pb:
                    current_collisions.add(a)
                    current_collisions.add(b)
        collisions = collisions.union(current_collisions)
        parts = [part for part in parts if part[0] not in collisions]

    return len(lines) - len(collisions)
