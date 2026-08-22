with open("DATA1.in") as f:
    set1 = set([word.lower() for word in f.read().split()])
with open("DATA2.in") as f:
    set2 = set([word.lower() for word in f.read().split()])
print(*sorted(set1 - set2))
print(*sorted(set2 - set1))