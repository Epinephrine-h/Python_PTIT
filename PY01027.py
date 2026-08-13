def check(n):
    for ch in n:
        if ch != '6' and ch != '8':     return False
    return n.find('888') == -1
print("YES" if check(input()) else "NO")