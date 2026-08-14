import math
import sys
imput = sys.stdin.readline
n, k = map(int, input().split())
cnt = 0
for num in range(10**(k - 1), 10**k):
    if math.gcd(num, n) == 1:
        cnt += 1
        print(num, end = " ")
    if cnt == 10:
        cnt = 0
        print()