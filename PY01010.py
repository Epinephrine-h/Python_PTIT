testcase = int(input())
for _ in range(testcase):
    s = input()
    print("YES" if s[:2] == s[-2:] else "NO")