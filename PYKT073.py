import sys
input = sys.stdin.readline
n = int(input().strip())
count_for_seven = 0
six_eight = False
ans = []
for _ in range(n):
    words = input().split()
    if len(words) == 7:
        if six_eight:
            ans.append(1)
            six_eight = False
        count_for_seven+=1
        if count_for_seven == 4:
            ans.append(2)
            count_for_seven = 0
    else:
        six_eight = True
if six_eight:   ans.append(1)
print(len(ans))
print(*ans, sep = '\n')
        