
A = 4
B = 3
target = 2
visited = set()
def dfs(a, b):
    if (a, b) in visited:
        return False
    print(a, b)
    visited.add((a, b))
    if a == target or b == target:
        print("Goal Reached!")
        return True
    states = [(A, b),  (a, B), (0, b),(a, 0),(a - min(a, B - b),b + min(a, B - b)),(a + min(b, A - a),b - min(b, A - a))]
    for x, y in states:
        if dfs(x, y):
            return True
    return False
dfs(0, 0)

       
