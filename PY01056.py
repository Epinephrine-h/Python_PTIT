import math
def isPrime(n):
    if n <= 1:  return False
    if n == 2:  return True
    if n % 2 == 0:  return False
    for num in range(3, int(math.sqrt(n) + 1), 2):
        if n % num == 0:    return False
    return True
def check(n):
    total = 0
    for i in range(len(n)):
        digit = ord(n[i]) - ord('0')
        if i % 2 == 0 and digit % 2 == 1:    return False
        if i % 2 == 1 and digit % 2 == 0:    return False
        total += digit
    return isPrime(total)
testcase = int(input())
for _ in range(testcase):
    print("YES" if check(input()) else "NO")