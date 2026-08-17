def solve(s):
    evenProduct, oddTotal = 1, 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != '0':  evenProduct *= ord(s[i]) - ord('0')
        if i % 2 == 1:      oddTotal += ord(s[i]) - ord('0')
    return [evenProduct, oddTotal]
testcase = int(input())
for _ in range(testcase):
    print(*solve(input()))