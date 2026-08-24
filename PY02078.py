testcase = int(input())
for _ in range(testcase):
    n = int(input())
    a, b = [0] * n, [0] * n
    for ith in range(n):
        a[ith], b[ith] = map(float, input().split())
    dp = [1] * n
    ans = 1
    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i] and b[j] > b[i]:     dp[i] = max(dp[i], dp[j] + 1)
        ans = max(ans, dp[i])
    print(ans)
        