testcase = int(input())
for _ in range(testcase):
    arr = list(input().strip())
    i = len(arr) - 2
    while i >= 0 and arr[i] <= arr[i+1]:     i-=1
    if i == -1:     print(-1)
    else:
        j = len(arr) - 1
        while arr[j] >= arr[i]:     j -= 1
        while j > i + 1 and arr[j] == arr[j-1]:     j-=1 
        arr[i], arr[j] = arr[j], arr[i]
        ans = "".join(arr)
        print(ans if ans[0] != '0' else -1)