import sys
def solve():
    data = sys.stdin.read().split()
    if not data:    return
    def search(arr, value, n):
        l, r, res = 0, n - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if (arr[mid] < value):
                res = mid
                l = mid + 1
            else:   r = mid - 1
        return res + 1
    testcase, idx = int(data[0]), 1
    out = []
    for _ in range(testcase):
        n = int(data[idx])
        idx+=1
        pos = list(map(int, data[idx:idx+n]))
        idx+=n
        h =  list(map(int, data[idx:idx+n]))
        idx+=n
        area, acc = [0] * n, [0] * n
        left_max, stack = [-1] * n, []
        for i in range(n):
            while stack and h[i] > h[stack[-1]]:   stack.pop()
            if not stack:   left_max[i] = -1
            else:   left_max[i] = stack[-1]
            stack.append(i)
        for i in range(n):
            if i == 0:
                area[i] = pos[i] * h[i]
                acc[i] = h[i]
            else:
                if h[i] <= h[i-1]:  area[i] = area[i-1] + (pos[i] - pos[i-1] - 1) * h[i]
                else:
                    if left_max[i] == -1:   area[i] = pos[i] * h[i] - acc[i-1]
                    else:
                        area[i] = area[left_max[i]] + (pos[i] - pos[left_max[i]] - 1) * h[i] - (acc[i-1] - acc[left_max[i]])
                acc[i] = acc[i-1] + h[i]
        q = int(data[idx])
        idx+=1
        while q:
            k = int(data[idx])
            q-=1
            idx+=1
            ans = search(area, k, n)
            out.append(ans)
    print(*out, sep = '\n')
if __name__ == '__main__':
    solve()

