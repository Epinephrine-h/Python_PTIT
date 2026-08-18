import math
n = int(input())
grid = [input() for _ in range(n)]
ans = 0
for i in range(n):
    tmp = 0
    for j in range(n):
        if grid[i][j] == 'C':   tmp += 1
    ans += math.comb(tmp, 2)
for i in range(n):
    tmp = 0
    for j in range(n):
        if grid[j][i] == 'C':   tmp += 1
    ans += math.comb(tmp, 2)
print(ans)