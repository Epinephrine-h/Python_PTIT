def check(n):
    r, tmp = 0, n
    while tmp:
        r = r * 10 + tmp % 10
        tmp //= 10
    return r == n
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
ans = -1
for x in matrix:
    for num in x:
        if check(num):      ans = max(ans, num)
if ans < 10:    print("NOT FOUND")
else:
    print(ans)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == ans:
                print(f"Vi tri [{i}][{j}]")