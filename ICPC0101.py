n = int(input())
arr = list(map(int,input().split()))
i = 0
final = []
for num in arr:
    if len(final) == 0:   final.append(num)
    else:
        if (final[-1] + num) % 2 == 0:  final.pop()
        else:   final.append(num)
print(len(final))