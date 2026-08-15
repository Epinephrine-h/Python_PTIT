import sys
all_data = sys.stdin.read().split()
it = iter(all_data)
arr = [int(next(it)) for _ in range(10)]
print(len(set(x % 42 for x in arr)))