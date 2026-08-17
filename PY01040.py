def Rotate(s):
    dist = 0
    for ch in s:
        dist += ord(ch) - ord('A')
    ans = []
    for ch in s:
        newChar = (ord(ch) - ord('A') + dist) % 26
        ans.append(chr(65 + newChar))
    return "".join(ans)
testcase = int(input())
for _ in range(testcase):
    s = input()
    divide = len(s) // 2
    s1 = Rotate(s[:divide])
    s2 = Rotate(s[divide:])
    ans = []
    for ch, dist in zip(s1, s2):
        newChar = (ord(ch) + ord(dist) - 2 * ord('A')) % 26
        ans.append(chr(newChar + 65))
    print("".join(ans))