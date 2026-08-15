import math
def reverse(n):
    ans = 0
    while n:
        ans = ans * 10 + n % 10
        n //=10
    return ans
#seive
limit = 1_000_001
prime = [True]*limit
prime[0] = prime[1] = False
for num in range(2, int(math.sqrt(limit) + 1)):
    if prime[num]:
        for d in range(2 * num, limit, num):    prime[d] = False
#run
testcase = int(input())
for _ in range(testcase):
    ans = []
    n = int(input())
    for i in range(13,n):
        if prime[i] and i not in ans:
            x = reverse(i)
            if prime[x] and x != i and x < n:
                ans.append(i)
                ans.append(x)
    for a in ans:   print(a, end = " ")
    print()