import math
def check(s):
    total = 0
    for ch in s:
        total += ord(ch) - ord('0')
    return total > 1 and all(total % num for num in range(2, int(math.sqrt(total) + 1)))
testcase = int(input())
for _ in range(testcase):
    print("YES" if check(input()) else "NO")