testcase = int(input())
for _ in range(testcase):
    n = int(input())
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    print("YES" if sum % 3 == 0 else "NO")