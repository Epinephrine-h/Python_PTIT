from collections import deque
def check(n):
    cnt = l = 0
    while n:
        digit = n % 10
        n //= 10
        if digit == 2:  cnt+=1
        l+=1
    return cnt > l // 2 
testcase = int(input())
d = deque([1,2])
tmp = []
while len(tmp) < 1001:
    cur = d.popleft()
    if check(cur):      tmp.append(cur)
    d.append(cur*10)
    d.append(cur*10+1)
    d.append(cur*10+2)
for _ in range(testcase):
    n = int(input())
    print(*tmp[:n])