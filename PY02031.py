import math
def isPrime(n):
    if n <= 1:  return False
    if n == 2:  return True
    if n % 2 == 0:  return False
    for num in range(3, int(math.sqrt(n) + 1), 2):
        if n % num == 0:    return False
    return True
n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        matrix[i][j] = 1 if isPrime(matrix[i][j]) else 0
for i in range(n):
    print(*matrix[i])