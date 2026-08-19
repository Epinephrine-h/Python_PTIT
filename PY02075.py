testcase = int(input())
for _ in range(testcase):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key = lambda x : (x[1], x[0]))
    prev, cnt = -1, 0
    for x in arr:
        if x[0] >= prev:
            cnt += 1
            prev = x[1]
    print(cnt)