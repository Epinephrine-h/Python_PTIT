s = input()
remainder = len(s) % 3
if remainder:
    s = s.zfill(len(s) + 3 - remainder)
ans = []
for i in range(0, len(s), 3):
    digit = int(s[i:i+3], 2)
    ans.append(str(digit))
print("".join(ans))