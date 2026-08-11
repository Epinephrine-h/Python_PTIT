def check(n):
    i = len(n) - 2
    while i > -1:
        if int(n[i]) > int(n[i + 1]):     return False
        i -= 1
    return True
testcase = int(input())
for _ in range(testcase):
    print("YES" if check(input()) else "NO")