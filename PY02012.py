import sys
data = sys.stdin.read().split()
n = int(data[0])
arr = [int(x) for x in data[1:]]
even = sorted([num for num in arr if num % 2 == 0])
odd = sorted([num for num in arr if num % 2 == 1])
e = 0
o = len(odd) - 1
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] = even[e]
        e += 1
    else:
        arr[i] = odd[o]
        o -= 1
print(*arr)