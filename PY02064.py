import sys
def solve():
    data = sys.stdin.read().split()
    if not data:    return
    testcase = int(data[0])
    coefs = [1, -2, 3, -4, 5]
    idx=1
    out = []
    for _ in range(testcase):
        n, k = int(data[idx]), int(data[idx+1])
        idx+=2
        arr = list(map(int, data[idx:idx+n]))
        idx+=n
        target = 5 * k
        if target == 0:
            out.append(0)
            continue
        dp = [float('-inf')] * (target + 1)
        dp[0] = 0
        for x in arr:
            for i in range(target, 0, -1):
                if dp[i-1] != float('-inf'):
                    c = coefs[(i-1)%5]
                    val = dp[i-1] + c*x
                    dp[i] = max(dp[i], val)
        out.append(dp[target])
    print(*out, sep = '\n')
if __name__ == '__main__':
    solve()
         