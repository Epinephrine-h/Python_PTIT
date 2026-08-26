testcase = int(input())
for _ in range(testcase):
    n = int(input())
    arr = list(map(int, input().split()))
    left_ptr = [0] * n
    right_ptr = [n - 1] * n
    for i in range(1, n):
        if arr[i] >= arr[left_ptr[i-1]]:    left_ptr[i] = i
        else:   left_ptr[i] = left_ptr[i-1]
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[right_ptr[i+1]]:    right_ptr[i] = i
        else:   right_ptr[i] = right_ptr[i+1]
    cnt = 0
    for i in range(n):
        if left_ptr[i] == right_ptr[i] == i:   cnt+=1
    print(cnt)