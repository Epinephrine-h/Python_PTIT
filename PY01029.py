import math
def reversingNumbers(n):
    ans = 0
    while n:
        ans = ans * 10 + n % 10
        n //= 10
    return ans
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    print("YES" if math.gcd(reversingNumbers(n), n) == 1 else "NO")