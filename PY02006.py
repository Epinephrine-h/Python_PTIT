testcase = int(input())
for _ in range(testcase):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("YES" if all(x <= y for x, y in zip(sorted(a), sorted(b))) else "NO")

