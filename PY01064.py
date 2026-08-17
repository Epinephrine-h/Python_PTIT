lenS = [0] * 27
lenS[0] = 0
for i in range(1,27):
    lenS[i] = lenS[i-1]*2 + 1
def divideAndConquer(n, k):
    mid = lenS[n-1] + 1
    if k == mid:      return chr(64 + n)
    elif k < mid:   return divideAndConquer(n-1, k)
    return divideAndConquer(n-1, k - mid)
testcase = int(input())
for _ in range(testcase):
    n, k = map(int, input().split())
    print(divideAndConquer(n, k))