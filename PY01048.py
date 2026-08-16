import math
def theNumberOfOddDivisor(n):
    cnt = 0
    for i in range(1, (int(math.sqrt(n)) + 1)):
        if n % i == 0:
            if i % 2 == 1:  cnt += 1
            if n // i != i and (n // i) % 2 == 1:     cnt += 1
    cnt -= 1
    return cnt
testcase = int(input())
for _ in range(testcase):
    print(theNumberOfOddDivisor(int(input())))