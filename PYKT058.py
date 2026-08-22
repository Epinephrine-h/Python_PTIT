testcase = int(input())
for _ in range(testcase):
    n, m , u, v = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
    visited = [False] * (n + 1)
    def dfs(u, ban):
        visited[u] = True
        for v in graph[u]:
            if v != ban and not visited[v]:     dfs(v, ban)
    ans = 0
    for i in range(1, n + 1):
        if i == u or i == v:    continue
        for x in range(n + 1):  visited[x] = False
        dfs(u, i)
        if not visited[v]:      ans+=1
    print(ans)
