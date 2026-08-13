import math
def isPrime(n):
    if n <= 1:      return False
    if n == 2:      return True
    if n % 2 == 0:      return False
    for num in range(3, int(math.sqrt(n) + 1), 2):
        if n % num == 0:    return False
    return True
prime = [x for x in range(10000) if isPrime(x)]
n, x = map(int, input().split())
print(x, end = " ")
for ith in range(n):
    x += prime[ith]
    print(x, end = " ")