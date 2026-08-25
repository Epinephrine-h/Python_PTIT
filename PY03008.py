n = int(input())
graph = [[] for _ in range(n + 1)]
for edge in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
def check():
    for adj in graph:
        if len(adj) == n - 1:   return "Yes"
    return "No"
print(check())