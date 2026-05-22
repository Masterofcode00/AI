from collections import deque
def valid(m, c):
    return (0 <= m <= 3 and 0 <= c <= 3 and(m == 0 or m >= c) and(3 - m == 0 or 3 - m >= 3 - c))
def bfs():
    q = deque([((3, 3, 1), [])])
    seen = set()
    while q:
        (m, c, b), path = q.popleft()
        if (m, c, b) in seen:
            continue
        seen.add((m, c, b))
        path = path + [(m, c, b)]
        if (m, c, b) == (0, 0, 0):
            return path
        for dm, dc in [(1,0), (2,0),(0,1), (0,2),(1,1)]:
            if b:
                nm, nc = m - dm, c - dc
            else:
                nm, nc = m + dm, c + dc
            if valid(nm, nc):
                q.append(((nm, nc, 1 - b), path))
sol = bfs()
for s in sol:
    print(s)
