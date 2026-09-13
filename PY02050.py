testcase = int(input())
for _ in range(testcase):
    n = int(input())
    arr = list(map(int, input().split()))
    stack = [-1]
    res = []
    for i in range(n):
        if len(stack) > 1:
            while len(stack) > 1 and arr[stack[-1]] <= arr[i]:   stack.pop()
        res.append(i - stack[-1])
        stack.append(i)
    print(*res)