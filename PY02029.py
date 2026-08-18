from collections import Counter
def solve(arr):
    most = arr[0][1]
    for x, y in arr:
        if y < most:    return x
    return "NONE"
n, m = map(int, input().split())
cnt = Counter(list(map(int, input().split())))
process = sorted(cnt.items(), key = lambda x : (-x[1], x[0]))
print(solve(process))