import sys
data = sys.stdin.read().split()
testcase = int(data[0])
idx = 1
res = []
for _ in range(testcase):
    a, b = map(int, data[idx:idx+2])
    idx+=2
    row = []
    def count_digit(n, d):
        cnt = 0
        p = 1
        while p <= n:
            high = n // (p * 10)
            cur = (n // p) % 10
            low = n % p
            if d == 0:
                if cur > 0:     cnt+=high * p
                elif cur == 0:      cnt+=(high - 1) * p + low + 1 
            else:
                if cur > d:
                    cnt+=(high + 1) * p
                elif cur == d:
                    cnt+=high * p + low + 1
                else:
                    cnt+=high * p
            p*=10
        return cnt
    for d in range(10):
        ans = count_digit(b, d) - count_digit(a - 1, d)
        row.append(ans)
    res.append(' '.join(map(str, row)))
print(*res, sep = '\n')