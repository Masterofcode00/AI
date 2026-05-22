
import heapq
def astar(g, s, t, h):
    q = [(0, s, [s])]
    v = set()
    while q:
        f, n, p = heapq.heappop(q)
        if n == t:
            return p
        if n in v:
            continue
        v.add(n)
        for x, c in g[n]:
            heapq.heappush(q,(len(p) + c + h(x),x,p + [x]))
g = {'A': [('B',1), ('C',3)],'B': [('D',1), ('E',3)],'C': [('F',5)],'D': [],'E': [('F',0)],'F': []}
h = lambda x: { 'A':5,'B':4,'C':2,'D':2,'E':1,'F':0}[x]
print(astar(g, 'A', 'F', h))

