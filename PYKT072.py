import sys
def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    if n == 1:      return 0
    arr = list(data[1:])
    origin = arr[0]
    m = [origin]
    for _ in range(len(origin)):
        new_str = m[-1][1:] + m[-1][0]
        if new_str not in m:    m.append(new_str)
    for s in arr:
        if s not in m:
            print(-1)
            return
    ans = float('inf')
    idxs = [m.index(s) for s in arr]
    for i in range(len(m)):
        tmp_cnt = 0
        for idx in idxs:
            tmp_cnt += i - idx if i >= idx else len(m) - idx + i
        ans = min(ans, tmp_cnt)
    print(ans)
if __name__ == '__main__':
    solve()