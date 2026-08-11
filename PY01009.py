s = input()
low = up = 0
for ch in s:
    if 'A' <= ch <= 'Z':    up += 1
    if 'a' <= ch <= 'z':    low += 1
print(s.lower() if low >= up else s.upper())