options = "2357"
n = int(input())
def step_by_n(n):
    x = ['0'] * n
    ans = []
    def check(arr):
        if arr[-1] == '2':  return False
        for digit in options:
            if digit not in arr:    return False
        return True
    def dfs(i):
        if i >= n:
            if check(x):
                ans.append("".join(x))
            return
        for digit in options:
            x[i] = digit
            dfs(i+1)
    dfs(0)
    print(*ans, sep = '\n')
for i in range(4, n + 1):
    step_by_n(i)
