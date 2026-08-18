import math
def isPrime(n):
    return n > 1 and all(n % num != 0 for num in range(2, int(math.sqrt(n) + 1)))
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = -1
for i in range(n):
    for j in range(m):
        if isPrime(arr[i][j]):
            ans = max(ans, arr[i][j])
if ans == -1:   print("NOT FOUND")
else:
    print(ans)
    for i in range(n):
        for j in range(m):
            if ans == arr[i][j]:
                print(f"Vi tri [{i}][{j}]")