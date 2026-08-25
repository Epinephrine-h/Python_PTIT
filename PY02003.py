import sys
import bisect
def solve():
    ham_nums = []
    p5 = 1
    while p5 <= 10**18:
        p3 = p5
        while p3 <= 10**18:
            p2 = p3
            while p2 <= 10**18:
                ham_nums.append(p2)
                p2*=2
            p3*=3
        p5*=5
    ham_nums.sort()
    def check(n):
        tmp = n
        for num in (2, 3, 5):
            while tmp % num == 0:
                tmp //= num
        if tmp != 1:      return "Not in sequence"
        return bisect.bisect(ham_nums, n)
    data = sys.stdin.read().split()
    testcase = int(data[0])
    ans = []
    for idx in range(1, testcase+1):
        n = int(data[idx])
        ans.append(check(n))
    print(*ans, sep = '\n')
solve()