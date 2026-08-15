import math
def isPrime(n):
    if n <= 1:  return False
    if n == 2:  return True
    if n % 2 == 0:  return False
    for num in range(3, int(math.sqrt(n) + 1), 2):
        if n % num == 0:    return False
    return True
testcase = int(input())
for _ in range(testcase):
    s = input()
    print("YES" if isPrime(int(s[-4:])) else "NO")