import sys
import math
def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    testcase = int(data[0])
    idx = 1
    out = []
    for _ in range(testcase):
        n, k = int(data[idx]), int(data[idx+1])
        idx+=2
        arr = list(map(int, data[idx:idx+n]))
        idx+=n
        ans = n + 1
        for i in range(n):
            if arr[i] == k:
                ans = 1
                break
            acc_div = arr[i]
            for j in range(i, n):
                acc_div = math.gcd(acc_div, arr[j])
                if acc_div <= k:
                    ans = min(ans, j - i + 1) if acc_div == k else ans
                    break
        out.append(ans if ans != n + 1 else -1)
    return out
if __name__ == '__main__':
    print(*solve(), sep = '\n')
            
            