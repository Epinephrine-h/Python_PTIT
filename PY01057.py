import math
prime = ['2', '3', '5', '7']
isPrime = [True] * 1000
isPrime[0] = isPrime[1] = False
for i in range(2, int(math.sqrt(1000) + 1)):
    if isPrime[i]:
        for j in range(i * i, 1000, i):     isPrime[j] = False
def check(s):
    for i in range(len(s)):
        if (isPrime[i] and s[i] not in prime) or (not isPrime[i] and s[i] in prime):    return False
    return True
testcase = int(input())
for _ in range(testcase):
    print("YES" if check(input()) else "NO")
    
