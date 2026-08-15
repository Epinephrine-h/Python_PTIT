testcase = int(input())
for _ in range(testcase):
    n = int(input())
    ans = 0
    start = 1 if n % 2 == 1 else 2
    for i in range(start,n + 1, 2):
        ans += (1/i)
    print("%.6f" % ans)