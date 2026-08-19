testcase = int(input())
for _ in range(testcase):
    word = input().split()
    cnt = i = 0
    ans = []
    while cnt < 100 and i < len(word):
        cnt += len(word[i])
        if cnt < 100:      ans.append(word[i])
        cnt += 1
        i+=1
    print(*ans)
"""
import textwrap
testcase = int(input())
for _ in range(testcase):
    print(textwrap.shorten(input(), width = 100, placeholder = ''))
"""