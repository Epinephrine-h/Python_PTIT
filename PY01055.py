def check(n):
    for i in range(2,len(n),2):
        if n[i - 2] != n[i]:    return False
    return len(n) % 2 == 1 and n[0] != n[1]
testcase = int(input())
for _ in range(testcase):
    print("YES" if check(input()) else "NO")