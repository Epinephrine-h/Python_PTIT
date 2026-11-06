import sys
def solve():
    data = sys.stdin.read().split()
    if not data:    return
    testcase = int(data[0])
    idx = 1
    ans = []
    for _ in range(testcase):
        n = int(data[idx])
        idx+=1
        x = list(int(num) for num in data[idx:idx+n])
        idx+=n
        x.sort()
        dp = [[float('inf')] * (2 * n + 1) for _ in range(n + 1)]
        for p in range(2 * n + 1):   dp[0][p] = 0
        for i in range(1, n + 1):
            for p in range(1, 2 * n + 1):
                dp[i][p] = min(dp[i][p-1], dp[i-1][p-1] + abs(x[i-1] - p))
        ans.append(dp[n][2*n])
    print(*ans, sep = '\n')
if __name__ == '__main__':
    solve()