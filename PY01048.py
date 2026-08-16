import math
def theNumberOfOddDivisors(n):
    cnt = 0
    for i in range(1, (int(math.sqrt(n)) + 1)):
        if n % i == 0:
            if i % 2 == 1:  cnt += 1
            if n // i != i and (n // i) % 2 == 1:     cnt += 1
    cnt -= 1
    return cnt
testcase = int(input())
for _ in range(testcase):
    print(theNumberOfOddDivisors(int(input())))
# 12 : 1 2 3 4 6 12 -> (3) 3 4 5
# 15 : 1 3 5 15 -> (3) 4 5 6; (5) 1 2 3 4 5; (15) '-6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6' 7 8
