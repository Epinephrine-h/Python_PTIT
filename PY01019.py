def check(s):
    i = 1
    while i < len(s):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s[-i]) - ord(s[-i-1])):       return False
        i += 1
    return True
testcase = int(input())
for _ in range(testcase):
    print("YES" if check(input())   else "NO")