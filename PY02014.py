import math
def isPrime(n):
    if n < 2:   return False
    if n == 2:  return True
    if n % 2 == 0:  return False
    for i in range(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:  return False
    return True
def binarySearch(p, x):
    left, right = 0, len(p) - 1
    ans = -1
    while left <= right:
        mid = (left + right)//2
        if p[mid] >= x:
            ans = mid
            right = mid - 1
        else:   left = mid + 1
    return ans
p = [num for num in range(2, 10050) if isPrime(num)]
setP = set(p)
n = int(input())
arr = list(map(int, input().split()))
ans = 0
for num in arr:
    if num not in setP:
        idx = binarySearch(p, num)
        dist_right = p[idx] - num
        if idx > 0:
            dist_left = num - p[idx-1] 
            min_dist = min(dist_left, dist_right)
        else:
            min_dist = dist_right
        ans = max(ans, min_dist)
print(ans)