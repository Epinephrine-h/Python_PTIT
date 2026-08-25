def dfs(current_node, banned_node):
    visited[current_node] = True
    for next_node in graph[current_node]:
        if next_node != banned_node and not visited[next_node]:     dfs(next_node, banned_node)
testcase = int(input())
for _ in range(testcase):
    n, m = map(int, input().split())
    graph = [[] for vertex in range(n + 1)]
    for edge in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    best = 1
    ans = None
    for u in range(1, n + 1):
        cnt= 0
        visited = [False] * (n + 1)
        for v in range(1, n + 1):
            if v == u:  continue
            if not visited[v]:
                cnt+=1
                dfs(v, u)
        if cnt > best:
            ans = u
            best = cnt
    print(0 if not ans else ans)
