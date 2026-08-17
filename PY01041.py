def check(s):
    if len(s) < 3:  return False
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:  return False
        if s[i] > s[i+1]:   break
        i += 1
    while i < len(s) - 1:
        if s[i] <= s[i+1]:  return False
        i += 1
    return True
testcase = int(input())
for _ in range(testcase):
    print("YES" if check(input()) else "NO")