import math
g = [[0] * 201 for _ in range(201)]
for i in range(201):
    for j in range(201):
        g[i][j] = math.gcd(i, j)
l, r = map(int, input().split())
for a in range(l, r - 1):
    for b in range(a + 1, r):
        if g[a][b] == 1:
            for c in range(b + 1, r + 1):
                if g[a][c] == 1 and g[b][c] == 1:
                    print(f"({a}, {b}, {c})")