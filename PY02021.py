testcase = int(input())
for _ in range(testcase):
    n, m, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    c = sorted(list(map(int, input().split())))
    i = j = l = 0
    ans = []
    while i < n and j < m and l < k:
        if a[i] == b[j] == c[l]:
            ans.append(a[i])
            i+=1
            j+=1
            l+=1
        elif a[i] <= b[j] and a[i] <= c[l]:     i+=1
        elif b[j] <= a[i] and b[j] <= c[l]:     j+=1
        elif c[l] <= a[i] and c[l] <= b[j]:     l+=1
    if not ans:     print("NO")
    else:   print(*ans)