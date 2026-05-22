g={'A':[['B','C'],['D']],'B':[],'C':[],'D':[]}
h={'A':int(input("A:")),'B':int(input("B:")),'C':int(input("C:")),'D':int(input("D:"))}
def ao(n):
    if g[n]==[]:
        return h[n]
    cost=[]
    for p in g[n]:
        s=0
        for c in p:
            s += ao(c)
        cost.append(s)
    return min(cost)
print("cost:",ao('A'))




'''
def ao(n):

    if g[n] == []:
        return h[n]

    cost = []

    for p in g[n]:

        s = 0

        for c in p:
            s += ao(c)

        cost.append(s)

    return min(cost)

print("Cost:", ao('A'))
'''
