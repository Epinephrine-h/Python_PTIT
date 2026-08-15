testcase = int(input())
for _ in range(testcase):
    n = int(input())
    ans = 0
    arr = list(map(int,input().split()))
    for num in arr:     ans ^= num
    print(ans)