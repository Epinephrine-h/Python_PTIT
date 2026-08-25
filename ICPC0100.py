import sys
data = sys.stdin.read().split()
testcase = int(data[0])
idx = 1
for _ in range(testcase):
    n = int(data[idx])
    idx+=1
    arr = [int(num) for num in data[idx:idx+n]]
    idx+=n
    ans = 0
    for i in range(0, n - 1):
        max_num = max(arr[i], arr[i+1])
        min_num = min(arr[i], arr[i+1])
        if max_num <= 2 * min_num:  continue
        while max_num > 2 * min_num:
            ans+=1
            min_num*=2
    print(ans)