import sys
import math
def isPrime(n):
    return n > 1 and all(n % num !=0 for num in range(2, int(math.sqrt(n) + 1)))
def check(arr):
    leftSum, totalSum = 0, sum(arr)
    for i in range(len(arr)):
        leftSum += arr[i]
        if isPrime(leftSum) and isPrime(totalSum - leftSum):    return i
    return "NOT FOUND"
data = sys.stdin.read().split()
n = int(data[0])
a = [int(x) for x in data[1:]]
b = []
for num in a:
    if num not in b:    b.append(num)
print(check(b))