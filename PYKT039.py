testcase = int(input())
def solve(a, b, n):
    for i in range(n):
        if a[i] > b[i]:     return False
    return True
for _ in range(testcase):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    print("YES" if solve(a, b, n) else "NO")
