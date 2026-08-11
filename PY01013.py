import math
def prime(n):
    if n <= 1:  return False
    if n == 2:  return True
    if n % 2 == 0:  return False
    for num in range(3, int(math.sqrt(n) + 1), 2):
        if n % num == 0:     return False
    return True
def number(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans
testcase = int(input())
for _ in range(testcase):
    a, b = map(int, input().split())
    print("YES" if prime(number(math.gcd(a, b))) else "NO")