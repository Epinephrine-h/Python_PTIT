import math
testcase = int(input())
for _ in range(testcase):
    n, x, m = map(float, input().split())
    print(int(math.log(m / n, (x + 100)/100)) + 1)