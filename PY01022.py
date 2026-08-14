n = input()
def cnt(n):
    if len(n) == 1:     return 0
    total = 0
    for ch in n:    total += ord(ch) - ord('0')
    return 1 + cnt(str(total))
print(1 if len(n) == 1 else cnt(n))