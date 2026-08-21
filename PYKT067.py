from itertools import permutations
import math
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    perms = list(permutations(range(1, n + 1)))
    print(math.factorial(n))
    print(*("".join(map(str, p)) for p in reversed(perms)))