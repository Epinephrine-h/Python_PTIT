import sys
def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n, q = int(data[0]), int(data[1])
    idx = 2
    d = [0] * (n + 2)
    for _ in range(q):
        x, y = int(data[idx]), int(data[idx+1])
        idx+=2
        d[x]+=1
        d[y+1]-=1
    res, cur = [], 0
    for i in range(1, n + 1):
        cur+=d[i]
        res.append(abs(cur%2))
    print(*res, sep = ' ')
if __name__ == '__main__':
    solve()