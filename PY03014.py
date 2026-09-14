testcase = int(input())
for _ in range(testcase):
    s = input()
    stack = []
    res = []
    cnt = 1
    for ch in s:
        if ch == '(':
            stack.append(cnt)
            res.append(cnt)
            cnt+=1
        elif ch == ')':
            res.append(stack.pop())
    print(*res)
