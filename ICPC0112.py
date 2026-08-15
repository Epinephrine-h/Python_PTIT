import math
limit = 1_000_001
prime = [True] * limit
prime[0] = prime[1] = False
for num in range(2, int(math.sqrt(limit) + 1)):
    if prime[num]:
        for d in range(2 * num, limit, num):    prime[d] = False
testcase = int(input())
for _ in range(testcase):
    n, cnt = int(input()), 0
    for num in range(2, n - 5):
        if prime[num] and prime[num + 6]:
            if prime[num + 2] or prime[num + 4]:    cnt += 1
    print(cnt)