import sys
class Matrix:
    def __init__(self, n, m, matrix):
        self.n = n
        self.m = m
        self.matrix = matrix
    def get_transpose(self):
        ans = []
        for j in range(self.m):
            row = []
            for i in range(self.n):     row.append(self.matrix[i][j])
            ans.append(row)
        return Matrix(self.m, self.n, ans)
    def multi(self, other):
        ans = []
        for i in range(self.n):
            row = []
            for j in range(other.m):
                tmp = 0
                for idx in range(self.m):   tmp += self.matrix[i][idx]*other.matrix[idx][j]
                row.append(tmp)
            ans.append(row)
        return ans
#I/O
data = sys.stdin.read().split()
testcase = int(data[0])
idx = 1
for _ in range(testcase):
    n, m = int(data[idx]), int(data[idx+1])
    idx+=2
    arr = []
    for _ in range(n):
        arr.append([int(x) for x in data[idx:idx+m]])
        idx+=m
    x = Matrix(n, m, arr)
    xt = x.get_transpose()
    ans = x.multi(xt)
    for row in ans:
        print(*row)
