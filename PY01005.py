n = int(input())
cnt = 0
while n:
    x = n % 10
    if x == 4 or x == 7:    cnt += 1
    n //= 10
print("YES" if cnt == 4 or cnt == 7 else "NO")