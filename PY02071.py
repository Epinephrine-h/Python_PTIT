testcase = int(input())
for _ in range(testcase):
    n = int(input())
    ans, tmp = [], [n]
    while True:
        ans.append(list(tmp))
        i = len(tmp) - 1
        while i >=0 and tmp[i] == 1:  i-=1
        if i < 0:   break
        remain = len(tmp) - i
        tmp[i]-=1
        del tmp[i+1:]
        best = tmp[-1]
        while remain:
            add = min(remain, best)
            tmp.append(min(remain, best))
            remain -= add
    print(len(ans))
    print(*(f"({' '.join(map(str, x))})" for x in ans))
