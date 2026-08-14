import math
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    ans = ["1"]
    for num in range(2, int(math.sqrt(n) + 1)):
        if n % num == 0:
            cnt = 0
            while n % num == 0:
                n //= num
                cnt+=1
            ans.append("*")
            ans.append(f"{num}^{cnt}")
    if n != 1:
        ans.append("*")
        ans.append(f"{n}^{1}")
    print(" ".join(ans))