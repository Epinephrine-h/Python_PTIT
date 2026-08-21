import sys
data = sys.stdin.read().split()
testcase = int(data[0])
idx = 1
for _ in range(testcase):
    n, c, d = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx+=3
    a = [int(money) for money in data[idx:idx+n]]
    idx+=n
    pre, nor = min(c, d), max(c, d)
    a.sort(reverse=True)
    wealthy = sum(a[:pre])/pre + sum(a[pre:pre+nor])/nor
    print(f"{wealthy:.6f}")