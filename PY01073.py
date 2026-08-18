import itertools
arr = list(input())
for x in itertools.permutations(arr):
    print("".join(x))