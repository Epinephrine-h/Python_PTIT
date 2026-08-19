code = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
bit = {4:2, 8:3, 16:4}
def convert(s, base):
    if base == 2:   return s
    remainder = len(s) % bit[base]
    s = "".join(['0']*((bit[base] - remainder) % bit[base])) + s
    ans = []
    for i in range(0, len(s), bit[base]):
        digit = int(s[i:i+bit[base]], 2)
        ans.append(format(digit, "X"))
    return "".join(ans)
with open("DATA.in", "r") as f:
    data = f.read().split()
    testcase = int(data[0])
    idx = 1
    for _ in range(testcase):
        base = int(data[idx])
        s = data[idx+1]
        idx += 2
        print(convert(s, base))