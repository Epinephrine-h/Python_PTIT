class Matrix:
    def __init__(self, n, m, matrix):
        self.n = n
        self.m = m
        self.matrix = matrix
    def get_transpose(self):
        transpose = []
        for j in range(self.m):
            row = []
            for i in range(self.n):    row.append(arr[i][j])
            transpose.append(row)
        return transpose
    def multi(self, other):
        ans = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                tmp = 0
                for idx in range(self.m):
                    tmp += self.matrix[i][idx]*other.matrix[idx][j]
                row.append(tmp)
            ans.append(row)
        return ans
testcase = int(input())
for _ in range(testcase):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    x = Matrix(n, m, arr)
    tx = Matrix(m, n, x.get_transpose())
    ans = x.multi(tx)
    for row in ans:
        print(*row)