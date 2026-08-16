import math
def check(n):
    prime = notPrime = cnt = 0
    valid = [2,3,5,7]
    while n:
        x = n % 10
        n //= 10
        if x in valid:  prime += 1
        else:   notPrime += 1
        cnt += 1
    return prime > notPrime and cnt > 1 and all(cnt % i != 0 for i in range(2, int(math.sqrt(cnt) + 1)))    
testcase = int(input())
for _ in range(testcase):
    print("YES" if check(int(input())) else "NO")