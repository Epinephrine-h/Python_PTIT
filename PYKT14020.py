import sys

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
        if n == 1:
            out.append((arr[0] // k) * k)
            continue
        lo, hi, ans = 1, 2*10**18, 0
        while lo <= hi:
            cnt, mid, tmp = 0, (lo + hi)//2, arr[0]
            for i in range(n-1):
                r = (tmp + arr[i+1])//mid
                tmp = min(arr[i+1],tmp + arr[i+1] - r * mid)
                cnt+=r
                if cnt >= k:  break
            if cnt >= k:
                ans, lo = mid, mid + 1
            else:
                hi = mid - 1
        out.append(str(ans*k))
    print(*out, sep = '\n')
if __name__ == '__main__':
    solve()
            