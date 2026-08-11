import math
def prime(n):
    if n <= 1:  return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:      return False
    return True
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    cnt = 0
    for num in range(1, n):
        if math.gcd(num, n) == 1:    cnt += 1
    print("YES" if prime(cnt) else "NO")