l1 = [word.lower() for word in input().split()]
l2 = [word.lower() for word in input().split()]
print(*sorted(set(l1) | set(l2)))
print(*sorted(set(l1) & set(l2)))