n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
if n == m:
    for row in matrix:
        print(*row)
elif n > m:
    diff = n - m
    i = 0
    while i < diff:
        matrix.pop(i)
        i+=1
    for row in matrix:
        print(*row)
else:
    diff = m - n
    i = 1
    while i < diff + 1:
        for x in matrix:
            x.pop(i)
        i+=1
    for row in matrix:
        print(*row)