n = int(input())
arr, total = [], 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    total+=sum(tmp)
    arr.append(tmp)
original_total = total//(2*(n-1))
if n == 2:
    print(1, original_total - 1)
else:
    res = [(sum(arr[i]) - original_total)// (n - 2) for i in range(n)]
    print(*res)