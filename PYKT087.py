import sys
MOD = 10**9 + 7
data = sys.stdin.read().split()
testcase = int(data[0])
idx = 1
for _ in range(testcase):
    n, k = int(data[idx]), int(data[idx+1])
    idx+=2
    binary = []
    while k:
        binary.append(k%2)
        k//=2
    ans = 0
    for i in range(len(binary)):
        if binary[i] == 1:
            ans += n**i%MOD
    print(ans%MOD)