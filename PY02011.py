n = int(input())
arr = list(map(int, input().split()))
ans, s = -1, float('inf')
for destination in arr:
    tmp = 0
    for num in arr:
        tmp += abs(destination - num)
    if tmp < s:
        ans = destination
        s = tmp
print(s, ans)