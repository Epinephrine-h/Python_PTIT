def memberTotal(x):
    total = 0
    while x:
        total += x % 10
        x //= 10
    return total
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(key=lambda x : (memberTotal(x), x))
    print(*arr)