def solve(n):
    n = str(n)
    mid = len(n) // 2
    left, right = int(n[:mid]), int(n[mid:])
    return left + right
n = int(input())
while n > 9:
    n = solve(n)
    print(n)