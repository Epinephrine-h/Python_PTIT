limit = 2**31
def check(s):
    if len(s) > 10 or s.isalpha() :     return True
    if (-1)*limit <= int(s) <= limit - 1:   return False
    return True
with open("DATA.in") as f:
    data = f.read().split()
    ans = []
    for n in data:
        if check(n):    ans.append(n)
    ans.sort()
    print(*ans)