def check(n):
    prev = n % 10
    n //= 10
    total = prev
    while n:
        cur = n % 10
        n //= 10
        if abs(cur - prev) != 2:    return False
        prev = cur
        total += cur
    return total % 10 == 0

testcase = int(input())
for _ in range(testcase):
    print("YES" if check(int(input())) else "NO")
    