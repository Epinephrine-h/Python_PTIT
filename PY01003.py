def rounding(n):
    rem = ans = 0
    acc = 1
    while n:
        x = n % 10
        acc *= 10
        n //= 10
        ans = x + 1 if rem >= 5 else x
        rem = ans
    return ans*acc//10
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    print(rounding(n))