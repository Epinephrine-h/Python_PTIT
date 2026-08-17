s = input()
remainder = (3 - (len(s) % 3)) % 3
s = "".join(['0']*remainder) + s
ans = []
for i in range(0,len(s), 3):
    ans.append(int(s[i:i+3], 2))
for digit in ans:   print(digit, end = "")