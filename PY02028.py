import math
import sys
prime = [True] * 2001
prime[0] = prime[1] = False
for i in range(2, int(math.sqrt(2001) + 1)):
    if prime[i]:
        for j in range(i*i, 2001, i):   prime[j] = False
data = sys.stdin.read().split()
n = int(data[0])
arr = [int(x) for x in data[1:]]
p = sorted([num for num in arr if prime[num]])
ptr = 0
for i in range(n):
    if prime[arr[i]]:
        arr[i] = p[ptr]
        ptr += 1
print(*arr)