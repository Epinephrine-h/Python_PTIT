def luckyNumber(n):
    while n:
        x = n % 10
        n //= 10
        if x != 4 and x != 7:   return False
    return True
testcase = int(input())
for _ in range(testcase):
    print("YES" if luckyNumber(int(input())) else "NO")