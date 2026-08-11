fibonacci = [0] * 93
fibonacci [0] = 0
fibonacci [1] = 1
for ith in range(2, 93):
    fibonacci[ith] = fibonacci[ith - 1] + fibonacci[ith - 2]
testcase = int(input())
for _ in range(testcase):
    a, b = map(int, input().split())
    for ith in range(a, b + 1):
        print(fibonacci[ith], end = " ")
    print()