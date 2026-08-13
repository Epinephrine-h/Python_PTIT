n = int(input())
attendance = [False] * 30001
arr = list(map(int, input().split()))
for num in arr:
    attendance[num] = True
for num in range(1,30001):
    if not attendance[num]:
        print(num)
        break