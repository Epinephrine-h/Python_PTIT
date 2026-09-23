import sys
import math
def solve():
    data = sys.stdin.read().split()
    if not data:    return
    testcase = int(data[0])
    idx = 1
    out = []
    for _ in range(testcase):
        n, k = int(data[idx]), int(data[idx+1])
        s = data[idx+2]
        idx+=3
        prefix = [0] * n
        prefix[0] = 1 if s[0] == '1' else 0
        for i in range(1, n):
            prefix[i] = prefix[i-1] + 1 if s[i] == '1' else prefix[i-1]
        ans = 0
        for i in range(n):
            if s[i] == '1':     ans += 2 * (prefix[min(n - 1, i + k)] - prefix[i])
        num, den = ans+prefix[n-1], n*n
        x = math.gcd(num, den)
        out.append(f"{num//x}/{den//x}" if num != 0 else "0/1")
    print(*out, sep ='\n')
if __name__ == '__main__':
    solve()