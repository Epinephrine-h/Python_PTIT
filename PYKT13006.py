import math
import sys
MOD = 1000
def matrix_mult(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0])%MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1])%MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0])%MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1])%MOD]
    ]
def matrix_pow(M, p):
    R = [[1, 0], [0, 1]]
    while p > 0:
        if p & 1:
            R = matrix_mult(R, M)
        M = matrix_mult(M, M)
        p>>=1
    return R
def a_mod(n):
    if n == 0:  return 2 % MOD
    M = [[6, -4], [1, 0]]
    Mp = matrix_pow(M, n - 1)
    return (Mp[0][0]*6 + Mp[0][1]*2) % MOD
def solve():
    data = sys.stdin.read().split()
    if not data:    return
    testcase = int(data[0])
    idx = 1
    for test in range(1, testcase+1):
        n = int(data[idx])
        idx+=1
        print(f"Case #{test}: {a_mod(n) - 1:03d}")  
if __name__ == '__main__':
    solve()