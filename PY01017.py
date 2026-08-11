testcase = int(input())
for _ in range(testcase):
    s = input()
    ans = []
    cnt = 1
    i = 1
    while i < len(s):
        if s[i] != s[i-1]:
            ans.append(str(cnt))
            ans.append(s[i-1])
            cnt = 1
        else:   cnt += 1
        i += 1
    ans.append(str(cnt))
    ans.append(s[-1])
    print("".join(ans))