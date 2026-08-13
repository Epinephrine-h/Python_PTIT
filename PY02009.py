testcase = int(input())
for _ in range(testcase):
    d = [0] * 1001
    n = int(input())
    for i in range(n):
        d[int(input())] += 1
    ans, record = -1, -1
    for ith in range(1,1001):
        if record < d[ith]:
            ans = ith
            record = d[ith]
    print(ans)