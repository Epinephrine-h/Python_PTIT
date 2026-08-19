import sys
data = sys.stdin.read().split()
n = int(data[0])
d = [False] * 201
arr = [int(x) for x in data[1:]]
for num in arr:     d[num] = True
end = max(arr)
ans = []
for num in range(1, end):
    if not d[num]:      ans.append(num)
if not ans:     print("Excellent!")
else:
    for num in ans:     print(num)