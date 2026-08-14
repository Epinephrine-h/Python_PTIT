while True:
    n = int(input())
    if n == 0: break
    small, big = float('inf'), float('-inf')
    for _ in range(n):
        num = input()
        i = 0
        while i < len(num) and num[i] == '0': i += 1
        if i == len(num):   num = 0
        small, big = min(small, int(num)), max(big, int(num))
    print("BANG NHAU" if small == big else f"{small} {big}")
