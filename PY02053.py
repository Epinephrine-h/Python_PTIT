n = int(input())
matrix = [ list(map(int, input().split())) for _ in range(n)]
k = int(input())
up = down = 0
for i in range(n):
    for j in range(n):
        if i + j < n - 1:   up+=matrix[i][j]
        if i + j > n - 1:   down+=matrix[i][j]
deviation = abs(up - down)
print("YES" if deviation <= k else "NO")
print(deviation)