import math
def check(n):
    tmp, krish = n, 0
    while tmp:
        x = tmp % 10
        tmp //= 10
        krish += math.factorial(x)
    return krish == n
testcase = int(input())
for _ in range(testcase):
    print("Yes" if check(int(input())) else "No")