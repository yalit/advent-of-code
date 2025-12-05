def handle_part_1(lines: list[str]) -> int:
    fresh = []
    for i, line in enumerate(lines):
        if line == "": break
        
        fresh.append(tuple(map(int, line.split('-'))))
    fresh = sorted(fresh)

    ingredients = sorted(list(map(int, lines[i+1:])))
    id_fresh = 0
    id_ing = 0
    total = 0
    while id_ing < len(ingredients) and id_fresh < len(fresh):
        a, b = fresh[id_fresh]
        ing = ingredients[id_ing]
        if ing < a: 
            id_ing += 1
            continue
        if a <= ing <= b:
            total += 1
            id_ing += 1
            continue
        id_fresh += 1

    return total

def handle_part_2(lines: list[str]) -> int:
    fresh = []
    for i, line in enumerate(lines):
        if line == "": break
        
        fresh.append(sorted(tuple(map(int, line.split('-')))))
    fresh = sorted(fresh)

    total = 0
    s,e = fresh[0]
    for i in range(1, len(fresh)):
        na, nb = fresh[i]
        if na > e:
            total += e-s + 1
            s, e = na, nb
            continue

        if nb < e:
            continue

        s,e = min(s,na), max(e,nb)
    total += e-s+1

    return total


