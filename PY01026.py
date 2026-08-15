from collections import Counter
testcase = int(input())
for ith in range(1,testcase + 1):
    s1 = input()
    s2 = input()
    print(f"Test {ith}:", end = " ")
    print("YES" if Counter(s1) == Counter(s2) else "NO")