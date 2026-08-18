n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
maxNum, minNum = 0, 10**5
for i in range(n):
    for j in range(m):
        maxNum = max(maxNum, arr[i][j])
        minNum = min(minNum, arr[i][j])
luckyNum = maxNum - minNum
ans = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == luckyNum:
            ans.append([i,j])
if not ans:     print("NOT FOUND")
else:
    print(luckyNum)
    for x in ans:
        print(f"Vi tri [{x[0]}][{x[1]}]")