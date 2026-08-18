n, k = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
for i in range(1, n):
    if abs(arr[i] - arr[i-1]) > k:      cnt+=1
print(cnt+1)