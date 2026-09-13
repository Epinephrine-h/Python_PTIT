import sys
input = sys.stdin.readline
n = int(input())
m = {}
t, cnt = None, 0
for _ in range(n):
    s = input().strip()
    if not t:
        t = s
        continue
    if not s:
        m[t] = cnt
        t = None
        cnt = 0
    else:
        cnt+=1
if t: m[t] = cnt
for topic, amount in m.items():
    print(f"{topic}: {amount}")
