def sievingChar(s):
    for i in range(0,len(s)):
        if i > 0 and s[i] == s[i-1] == '.':   return False
        if s[i] != '.' and s[i] not in "0123456789":    return False
    return True
testcase = int(input())
for _ in range(testcase):
    s = input()
    if not sievingChar(s):
        print("NO")
        continue
    numbers = list(map(int, s.split('.')))
    print("YES" if len(numbers) == 4 and all(0 <= n <= 255 for n in numbers) else "NO")