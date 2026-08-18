s = input()
ans = set()
n = len(s) if len(s) % 2 == 0 else len(s) - 1
for i in range(0, n, 2):
    ans.add(int(s[i:i+2]))
print(*sorted(ans))