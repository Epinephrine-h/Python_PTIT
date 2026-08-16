testcase = int(input())
for _ in range(testcase):
    n = int(input())
    d = [False] * 1001
    arr = list(map(int, input().split()))
    start, end = 1001, 0
    for num in arr:
        d[num] = True
        start = min(start, num)
        end = max(end, num)
    cnt = 0
    for num in range(start, end):
        if not d[num]:      cnt += 1
    print(cnt)