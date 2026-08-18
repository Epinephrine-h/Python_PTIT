s = input()
k = int(input())
ans = []
d = [0] * 100
n = len(s) if len(s) % 2 == 0 else len(s) - 1
for i in range(0, n, 2):
    num = int(s[i:i+2])
    if num not in ans:  ans.append(num)
    d[num]+=1
found = False
ans.sort()
for num in ans:
    if d[num] >= k:
        found = True
        print(num, d[num])
if not found:   print("NOT FOUND")