n = int(input())
arr = sorted(list(map(float, input().split())))
minptr, maxptr = 1, n - 2
while minptr < n and arr[minptr] == arr[minptr-1]:     minptr += 1
while maxptr >=0 and arr[maxptr] == arr[maxptr+1]:     maxptr -= 1
total = sum(arr[minptr:maxptr+1])
ans = total / (maxptr - minptr +1)
print("%.2f" % ans)