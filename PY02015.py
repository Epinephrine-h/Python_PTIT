def step(arr):
    cnt, n = 0, len(arr)
    while max(arr) != min(arr):
        cnt += 1
        tmp = arr[0]
        for i in range(n):
            if i == n - 1:  arr[i] = abs(arr[i] - tmp)
            else: arr[i] = abs(arr[i] - arr[i+1])
    return cnt
while True:
    arr = list(map(int, input().split()))
    if max(arr) == min(arr) == 0:   break
    print(step(arr))