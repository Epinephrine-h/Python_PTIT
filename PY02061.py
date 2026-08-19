testcase = int(input())
for _ in range(testcase):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    kernel = [list(map(int, input().split())) for _ in range(3)]
    convolution = []
    for i in range(0, n - 2):
        row = []
        for j in range(0, m - 2):
            e = 0
            for x in range(3):
                for y in range(3):
                    e += matrix[i+x][j+y] * kernel[x][y]
            row.append(e)
        convolution.append(row)
    ans = 0
    for row in convolution:
        ans += sum(row)
    print(ans)