n = int(input())
seen = set()
cnt = 0
for _ in range(n):
    s = input()
    if s not in seen:
        cnt += 1
        seen.add(s)
print(cnt)