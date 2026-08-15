def reverse(n):
    ans = 0
    while n:
        ans = ans * 10 + n % 10
        n //= 10
    return ans
testcase = int(input())
for _ in range(testcase):
    exist = False
    n = int(input())
    for step in range(1000):
        if n % 7 == 0:
            exist = True
            break
        n += reverse(n)
    print(n if exist else -1)