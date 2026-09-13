from collections import Counter
n, k = map(int, input().split())
data = []
for _ in range(n):
    s = input().strip().lower()
    tmp = []
    for c in s:
        if not c.isalnum():     tmp.append(' ')
        else:   tmp.append(c)
    data.extend(''.join(tmp).split())
cnt = Counter(data)
ls = sorted(cnt.keys(), key = lambda x : (-cnt[x], x))
for x in ls:
    if cnt[x] < k:  break
    print(x, cnt[x]) 