def checkQuantity(n):
    cnt = 0
    while n:
        x = n % 10
        cnt += 1
        if x % 2 != 0:  return False
        n //= 10
    return cnt % 2 == 0
def palidrome(n):
    n = str(n)
    i, j = 0, len(n) - 1
    while i <= j:
        if n[i] != n[j]:    return False
        i += 1
        j -= 1
    return True
testcase = int(input())
for _ in range(testcase):
    for num in range(22, int(input())):
        if checkQuantity(num) and palidrome(num):   print(num, end = " ")
    print()