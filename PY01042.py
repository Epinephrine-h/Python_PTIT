def check(s):
    for ch in s:
        if not ('0' <= ch <= '2'):      return False
    return True
testcase = int(input())
for _ in range(testcase):
    print("YES" if check(input()) else "NO")