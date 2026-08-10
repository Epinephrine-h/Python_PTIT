testcase = int(input())
bit = {4: 2, 8 : 3, 16 : 4}
hexa = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
def convert(b, s):
    if b == 2:      return s
    s = '0' * ((bit[b] - len(s) % bit[b]) % bit[b]) + s
    ans = []
    for i in range(0, len(s), bit[b]):
        group = s[i : i + bit[b]]
        c = int(group, 2)
        ans.append(c)
    for i in range(len(ans)):
        if ans[i] >= 10:    ans[i] = hexa[ans[i]]
    for i in range(len(ans)):   ans[i] = str(ans[i])
    return "".join(ans) 
        
while testcase:
    testcase -= 1

    b = int(input())
    s = input()
    print(convert(b, s))
