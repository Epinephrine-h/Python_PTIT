def check(n):
    r, tmp = 0, n
    while n:
        r = r * 10 + n % 10
        n //= 10
    return r == tmp
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = -1
for i in range(n):
    for j in range(m):
        if check(arr[i][j]):
            ans = max(ans, arr[i][j])
if ans == -1 or ans < 10:   print("NOT FOUND")
else:
    print(ans)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == ans:    print(f"Vi tri [{i}][{j}]")