'''
n = int(input("Enter n value: "))
b = [-1] * n
def ok(r, c):
    for i in range(r):
        if (b[i] == c or abs(b[i] - c) == abs(i - r)):
            return False
    return True
def solve(r=0):
    if r == n:
        print(b)
        return True
    for c in range(n):
        if ok(r, c):
            b[r] = c
            if solve(r + 1):
                return True
            b[r] = -1
    return False
solve()



'''
n=int(input("enter the n value"))
b=[-1]*n
def ok(r,c):
    for i in range(r):
        if (b[i]==c or abs(b[i]-c)==abs(i-r)):
            return False
    return True
def solve(r=0):
    if r==n:
        print(b)
        return True
    for c in range(n):
        if ok(r,c):
            b[r]=c
        if solve(r+1):
            return True
        b[r] = -1
    return False
solve()

