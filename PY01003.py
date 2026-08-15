def rounding(n):
    if n == 0:      return 0
    carry = 0
    lengthOfNumber = 0
    while n:
        currentDigit = n % 10
        lengthOfNumber += 1
        n //= 10
        rounded = currentDigit + 1 if carry >= 5 else currentDigit
        carry = rounded
    return carry * (10 ** (lengthOfNumber - 1))
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    print(rounding(n))
