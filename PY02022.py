from collections import Counter
import math
def isPrime(n):
    return n > 1 and all(n % num for num in range(2, int(math.sqrt(n) + 1)))
n = int(input())
arr = list(map(int, input().split()))
cnt = Counter(arr)
for num in arr:
    if cnt[num] > 0 and isPrime(num):
        print(num, cnt[num])
        cnt[num] = 0