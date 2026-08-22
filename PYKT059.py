def dfs(current_node):
    visited[current_node] = True
    for next_node in graph[current_node]:
        if not visited[next_node]:  dfs(next_node)
n, m, x = map(int, input().split())
graph = [[] for vertex in range(n+1)]
visited = [False]*(n+1)
for e in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(x)
for vertex in range(1, n + 1):
    if not visited[vertex]:     print(vertex)