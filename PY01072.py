import itertools
n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = itertools.combinations(sorted(set(arr)), k)
for x in result:
    print(*x)