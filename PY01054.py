testcase = int(input())
for _ in range(testcase):
    n = int(input())
    product = 1
    while n:
        x = n % 10
        n //= 10
        if x == 0:  continue
        product *= x
    print(product)