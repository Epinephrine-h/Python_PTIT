s = input()
n = len(s) if len(s) % 2 == 0 else len(s) - 1
ans = []
for i in range(0, n, 2):
    num = int(s[i:i+2])
    if num not in ans:      ans.append(num)
print(*ans)