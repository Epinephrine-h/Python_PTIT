def palindromeNumber(n):
    if n < 10:  return False
    tmp, rvs = n, 0
    while tmp:
        rvs = rvs * 10 + tmp % 10
        tmp //= 10
    return n == rvs
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    total = 0
    while n:
        total += n % 10
        n //= 10
    print("YES" if palindromeNumber(total) else "NO")