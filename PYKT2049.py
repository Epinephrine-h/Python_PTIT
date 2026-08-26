parent = [i for i in range(100_001)]
def find(v):
    while parent[v] != v:
        parent[v] = parent[parent[v]]
        v = parent[v]
    return v
def union(a, b):
    ax, bx = find(a), find(b)
    if ax != bx:
        parent[ax] = bx
def check(a, b):
    return 1 if find(a) == find(b) else 0
q = int(input())
for _ in range(q):
    x, y, z = map(int, input().split())
    if z == 1:
        union(x, y)
    else:
        print(check(x, y))