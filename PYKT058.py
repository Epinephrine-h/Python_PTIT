testcase = int(input())
for _ in range(testcase):
    n, m, u, v = map(int, input().split())
    graph = [[] for vertex in range(n+1)]
    for e in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
    def dfs(cur_node, banned_node):
        visited[cur_node] = True
        for next_node in graph[cur_node]:
            if next_node != banned_node and not visited[next_node]:     dfs(next_node, banned_node)
    ans = 0
    for i in range(1, n + 1):
        if i == u or i == v:    continue
        visited = [False]*(n+1)
        dfs(u, i)
        if not visited[v]:  ans+=1
    print(ans)
