from collections import Counter
n = int(input())
data = []
for _ in range(n):
    s = input().strip().lower()
    tmp = []
    for ch in s:
        if 'a' > ch or ch > 'z':     tmp.append(' ')
        else:   tmp.append(ch)
    data.extend(''.join(tmp).split())
cnt = Counter(data)
k = sorted(cnt.keys(), key = lambda x : (-cnt[x], x))
for x in k:
    print(x, cnt[x])
