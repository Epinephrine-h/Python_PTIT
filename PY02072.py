n = int(input())
arr = list(map(int, input().split()))
max_val = max(arr)
ans = cnt = 0
for i in range(n):
    if arr[i] == max_val:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
print(max(ans, cnt))