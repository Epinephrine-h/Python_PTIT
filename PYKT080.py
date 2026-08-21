m, n = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(m)]
idx = [-1,-1,-1,0,0,1,1,1]
idy = [-1,0,1,-1,1,-1,0,1]
visited = [[False]*n for _ in range(m)]
ans = 0
for i in range(m):
    for j in range(n):
        if city[i][j] == -1:
            for cell in range(8):
                tmpx = i + idx[cell]
                tmpy = j + idy[cell]
                if 0 <= tmpx < m and 0 <= tmpy < n and not visited[tmpx][tmpy]:
                    ans += city[tmpx][tmpy]
                    visited[tmpx][tmpy] = True
print(ans)