import sys
data = sys.stdin.buffer.read().split()
n, k = int(data[0]), int(data[1])
arr = map(int, data[2:])
ans = sum(1 for x in arr if x % k == 0)
print(ans)