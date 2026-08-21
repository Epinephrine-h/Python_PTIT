import math
import bisect
def solve():
    n = int(input())
    def binarySearch(l, r, lst, x):
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if lst[mid] <= x:
                ans = mid
                l = mid + 1
            else:   r = mid - 1
        return ans
    def isPrime(n):
        if n < 2:   return False
        if n == 2:  return True
        if n % 2 == 0:  return False
        for i in range(3, int(math.sqrt(n) + 1), 2):
            if n % i == 0:      return False
        return True
    prime = [num for num in range(2, int(math.sqrt(1_000_000_000) + 1)) if isPrime(num)]
    exp_8 = [2,3,5,7,11,13,17,19,23]
    cnt = 0
    for num in exp_8:
        if num**8 <= n:     cnt+=1
        else:   break
    for p in range(len(prime)):
        x = int(math.sqrt(n))//prime[p]
        pos = binarySearch(p + 1, len(prime) - 1, prime, x)
        if pos == -1:   break
        cnt+=pos - p
    print(cnt)
solve()