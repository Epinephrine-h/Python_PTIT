testcase = int(input())
for _ in range(testcase):
    n = int(input())
    u = float(input())
    arr = list(map(float, input().split()))
    arr.sort()
    for i in range(1, n):
        need = arr[i] - arr[i-1]
        if u < need * i:
            ideal = (sum(arr[:i]) + u)/i
            u = 0
            arr[:i] = [ideal]*i
            break
        else:
            arr[:i] = [arr[i]]*i
            u-=need*i
    if u > 0:
        for i in range(n):
            arr[i]+=u/n
    res=1
    for p in arr:   res*=p
    print(f"{res:.6f}")