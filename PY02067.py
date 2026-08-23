import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
min_a = min(a)

best = None
for k in range(min_a + 1):
    total = 0
    valid = True
    for x in a:
        b = x // (k + 1) + 1
        if x // b != k:
            valid = False
            break
        total += b
    if valid and (best is None or total < best):
        best = total

print(best)