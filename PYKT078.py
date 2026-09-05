testcase = int(input())
for _ in range(testcase):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    ans, tmp = [], []
    best = max(arr)
    for i in range(n):
        if arr[i] == best:
            arr.insert(i, m)
            break
    for num in arr:
        if num < 0:     ans.append(num)
        else:   tmp.append(num)
    ans.extend(tmp)
    print(*ans)