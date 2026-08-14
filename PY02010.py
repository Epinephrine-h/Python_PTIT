while True:
    n = int(input())
    if n == 0: break
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    print(f"{arr[0]} {arr[-1]}" if arr[0] != arr[-1] else "BANG NHAU")
