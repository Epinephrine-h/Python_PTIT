import sys
data = sys.stdin.read().split()
n, k = int(data[0]), int(data[1])
a = [int(cost) for cost in data[2:2+n]]
b = [int(cost) for cost in data[2+n:]]
before = sum(a)
decrease = sorted([a[i] - b[i] for i in range(n)], reverse = True)
saved = 0
for i in range(n - k):
    if decrease[i] > 0:
        saved += decrease[i]
    else:   break
print(before - saved)