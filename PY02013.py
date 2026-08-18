while True:
    n = int(input())
    if n == 0:  break
    seen = set()
    while n != 1:
        seen.add(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    print(len(seen) + 1)