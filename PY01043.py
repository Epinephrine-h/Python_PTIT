def palidromeAndEven(n):
    reverse, tmp = 0, n
    while tmp:
        x = tmp % 10
        tmp //= 10
        reverse = reverse * 10 + x
        if x % 2 != 0:  return False
    return reverse == n
testcase = int(input())
predict =  [x for x in range(22, 89) if palidromeAndEven(x)] + [x for x in range(2002, 8889) if palidromeAndEven(x)]
predict += [x for x in range(200002, 888889) if palidromeAndEven(x)]
for _ in range(testcase):
    n = int(input())
    for num in predict:
        if num >= n:    break
        print(num, end = " ")
    print()