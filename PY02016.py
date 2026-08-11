from collections import Counter
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    cnt = Counter(map(int, input().split()))
    best_key = max(cnt, key = cnt.get)
    print(best_key if cnt[best_key] > n//2 else "NO")