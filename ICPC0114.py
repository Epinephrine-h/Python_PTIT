import math
def isPrime(n):
    if n <= 1:      return False
    if n == 2:      return True
    if n % 2 == 0:      return False
    for num in range(3, int(math.sqrt(n) + 1), 2):
        if n % num == 0:    return False
    return True
def reverseNum(n):
    ans = 0
    while n:
        ans = ans * 10 + n % 10
        n //= 10
    return ans
def checkMember(n):
    total = 0
    while n:
        x = n % 10
        if x != 2 and x != 3 and x != 5 and x != 7:    return False
        total += x
        n //= 10
    return isPrime(total)
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    if not checkMember(n):
        print("No")
        continue
    if not isPrime(n):
        print("No")
        continue
    if not isPrime(reverseNum(n)):
        print("No")
        continue
    print("Yes")
