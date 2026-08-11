def convert(x, a, b):
    ans = str(x).replace(str(a), str(b))
    return int(ans)

testcase = int(input())
for _ in range(testcase):
    a, b = map(int,input().split())
    x = input().strip()
    if (x.count(" ")):  x, y = x.split()
    else:   y = input()
    x= int(x)
    y= int(y)
    if a > b:   a, b = b, a
    min_sum = convert(x, b, a) + convert(y, b, a)
    max_sum = convert(x, a, b) + convert(y, a, b)
    print(f"{min_sum} {max_sum}")