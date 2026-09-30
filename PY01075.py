import sys
from math import gcd
def solve():
    data = sys.stdin.read().split()
    if not data:    return
    testcase, idx, out = int(data[0]), 1, []
    for _ in range(testcase):
        n = int(data[idx]); idx+=1
        step = list(map(int, data[idx:idx+n])); idx+=n
        cost = list(map(int, data[idx:idx+n])); idx+=n
        dp = {0: 0}
        for i in range(n):
            for g, c in list(dp.items()):
                ng = gcd(g, step[i])
                nc = c + cost[i]
                if ng not in dp or dp[ng] > nc:
                    dp[ng] = nc
        out.append(dp.get(1, -1))
    print(*out, sep = '\n')
if __name__ == '__main__':
    solve() 