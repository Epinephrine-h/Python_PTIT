c = {10 + i : chr(i + 65) for i in range(26)}
def convert(n, base):
    ans = []
    while n:
        ans.append(n % base)
        n //= base
    for i in range(len(ans)):
        if ans[i] > 9:      ans[i] = c[ans[i]]
        else:   ans[i] = chr(ans[i] + 48)
    return "".join(ans[::-1])
testcase = int(input())
for _ in range(testcase):
    n, base = map(int, input().split())
    print(convert(n, base))