a, k, n = map(int, input().split())
b = k - a % k + a
hasAnswer = False
for num in range(b, n + 1, k):
    hasAnswer = True
    print(num - a, end = " ")
if not hasAnswer:   print(-1)