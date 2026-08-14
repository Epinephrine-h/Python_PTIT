import math
n, m = map(int, input().split())
current_total = sum(map(int, input().split()))
k = m - current_total
MOD = 1_000_000_007
print(int(math.comb(k + n - 1, n - 1)) % MOD)