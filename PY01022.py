n = input()
def cnt(n):
    if len(n) == 1:     return 0
    total = sum(ord(ch) - 48 for ch in n)
    return 1 + cnt(str(total))
print(1 if len(n) == 1 else cnt(n))
