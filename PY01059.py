def solve(s):
    zero = True
    evenTotal,oddProduct = 0,1
    for i in range(len(s)):
        if i % 2 == 1 and s[i] != '0':
            zero = False
            oddProduct *= (ord(s[i]) - ord('0'))
        if i % 2 == 0:  evenTotal += (ord(s[i]) - ord('0'))
    return [evenTotal, oddProduct] if not zero else [evenTotal, 0]
testcase = int(input())
for _ in range(testcase):
    print(*solve(input()))