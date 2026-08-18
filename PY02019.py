import sys
import math
data = sys.stdin.read().split() 
n = int(data[0])
arr = sorted([int(x) for x in data[1:]])
for i in range(n-1):
    for j in range(i + 1, n):
        if math.gcd(arr[i], arr[j]) == 1:
            print(arr[i], arr[j])