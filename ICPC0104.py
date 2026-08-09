testcase = int(input())
while testcase:
    testcase -= 1
    s = input()
    ans = float('inf')
    tmp = 0
    for i in range(len(s)):
        if 'a' <= s[i] <= 'z':
            if i > 0 and '0' <= s[i-1] <= '9':  ans = min(ans, tmp)
            tmp = 0
        else:   tmp = tmp * 10 + int(s[i])
    if '0' <= s[-1] <= '9':     ans = min(ans, tmp)
    print(ans)