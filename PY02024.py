def product(n):
    p = 1
    while n:
        p *= n % 10
        n //= 10
    return p
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(key=lambda x: (product(x), x))
    print(*arr)