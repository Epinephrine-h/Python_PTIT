import math
def isPrime(n):     return n > 1 and all(n % num != 0 for num in range(2, int(math.sqrt(n) + 1)))
def check(b):
    leftSum, totalSum = 0, sum(b)
    for i in range(len(b)):
        leftSum += b[i]
        if isPrime(leftSum) and isPrime(totalSum - leftSum):    return i
    return "NOT FOUND"
n = int(input())
arr = list(map(int, input().split()))
b = []
for num in arr:
    if num not in b:    b.append(num)
print(check(b))