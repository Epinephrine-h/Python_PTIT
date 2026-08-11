testcase = int(input())
for _ in range(testcase):
    s = input()
    i, j = 0, 1
    ans = []
    while j < len(s):
        ans += [s[i]] * int(s[j])
        i += 2
        j += 2
    print("".join(ans))
    