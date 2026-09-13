import sys
input = sys.stdin.readline
n = int(input())
res, t, cnt = {}, None, 0
for _ in range(n):
    s = input().strip()
    if not t:
        t = s
        continue
    if not s:
        res[t] = cnt
        t, cnt = None, 0
    else:   cnt+=1
if t:   res[t] = cnt
for topic, amount in res.items():
    print(f"{topic}: {amount}")