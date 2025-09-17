dirs = {
    # dq, dr, ds as seen here https://www.redblobgames.com/grids/hexagons/#neighbors
    'n': (0, -1, 1),
    'ne': (1, -1, 0),
    'se': (1, 0, -1),
    's': (0, 1, -1),
    'sw': (-1, 1, 0),
    'nw': (-1, 0, 1)
}

def handle_part_1(lines: list[str]) -> int:
    sq,sr,ss = 0,0,0

    q,r,s = sq,sr,ss
    for d in lines[0].split(','):
        dq, dr, ds = dirs[d]
        q,r,s = q+dq, r+dr, s+ds

    return hex_dist((q,r,s), (sq,sr,ss))


def handle_part_2(lines: list[str]) -> int:
    sq,sr,ss = 0,0,0
    m_dist = 0
    q,r,s = sq,sr,ss
    for d in lines[0].split(','):
        dq, dr, ds = dirs[d]
        q,r,s = q+dq, r+dr, s+ds
        m_dist = max(m_dist, hex_dist((q,r,s), (sq,sr,ss)))  
    return m_dist


def hex_dist(a, b):
    sq, sr, ss = a
    q,r,s = b
    return (abs(sq-q)+abs(sr-r)+abs(ss-s))//2