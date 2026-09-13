import sys
def solve():
    input = sys.stdin.readline
    testcase = int(input())
    res = []
    for _ in range(testcase):
        n, k = map(int, input().split())
        arr = sorted(list(map(int, input().split())))
        pre_sum = [0] * (n+1)
        pre_sum[0] = 0
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + arr[i]
        def ok(x):
            l, r = 0, n - 1
            fi = -1
            while l <= r:
                mid = (l + r)//2
                if arr[mid] > x:
                    fi, r = mid, mid - 1
                else:   l = mid + 1
            total = pre_sum[n] if fi == -1 else pre_sum[fi] + x * (n - fi)
            return total >= x * k
        lo, hi = 0, 2*10**18
        while lo < hi:
            mid = (lo + hi + 1)//2  
            if ok(mid):     lo = mid
            else:   hi = mid - 1
        res.append(lo)
    print(*res, sep = '\n')
if __name__ == '__main__':
    solve()