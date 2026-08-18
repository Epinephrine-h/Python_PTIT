n = int(input())
ans = []
for _ in range(n):
    s = input()
    tmp = 0
    for i in range(len(s)):
        if s[i].isdigit():
            tmp = tmp * 10 + ord(s[i]) - ord('0')
        else:
            if i > 0 and s[i-1].isdigit():      ans.append(tmp)
            tmp = 0
    if s[-1].isdigit():     ans.append(tmp)
ans.sort()
for num in ans:
    print(num)