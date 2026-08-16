import itertools
m, n = map(int, input().split())
s = sorted(set(input().split()))
result = itertools.combinations(s, n)
for x in result:
    print(*x)