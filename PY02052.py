n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
up = down = 0
for i in range(n):
    for j in range(n):
        if i > j:   down += matrix[i][j]
        if i < j:   up += matrix[i][j]
deviation = abs(up - down)
print("YES" if deviation <= k else "NO")
print(deviation)