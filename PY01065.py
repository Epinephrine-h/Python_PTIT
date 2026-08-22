cz = [1,6,11]
cnz = [0,5,10]
num = "0123456789"
op = "+-*/"
testcase = int(input())
for _ in range(testcase):
    ans = []
    def check(s):
        comps = s.split()
        a, b, c = int(comps[0]), int(comps[2]), int(comps[4])
        if comps[1] == '+' and a + b == c:      return True
        if comps[1] == '-' and a - b == c:      return True
        if comps[1] == '*' and a * b == c:      return True
        if comps[1] == '/' and a % b == 0 and a //b == c:   return True
        return False
    def dfs(s):
        if ans: return
        pos = s.find('?')
        if pos == -1:
            if check(s):
                ans.append(s)
        elif pos in cz:
            for digit in num:
                dfs(s.replace('?', digit, 1))
        elif pos in cnz:
            for digit in num[1:]:
                dfs(s.replace('?', digit, 1))
        else:
            for o in op:
                dfs(s.replace('?', o, 1))
    s = input()
    dfs(s)
    print(ans[0] if ans else "WRONG PROBLEM!")
