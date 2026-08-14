testcase = int(input())
for _ in range(testcase):
    s = input()
    ans = []
    totalOfDigits = 0
    for ch in s:
        if '0' <= ch <= '9':    totalOfDigits += int(ch)
        else:   ans.append(ch)
    ans.sort()
    ans.append(str(totalOfDigits))
    print("".join(ans))