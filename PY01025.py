n = int(input())
ans, cnt = [], 0
while n:
    if cnt == 3:
        ans.append(",")
        cnt = 0
    ans.append(str(n % 10))
    cnt += 1
    n //= 10
print("".join(ans[::-1]))