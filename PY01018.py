P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    test = input().split()
    if len(test) == 1 and int(test[0]) == 0:    break
    k, s = int(test[0]), test[1]
    ans = []
    for ch in s:
        ans.append(P[(P.find(ch) + k) % 28])
    print("".join(ans[::-1]))