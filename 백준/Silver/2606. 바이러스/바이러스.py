n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def dfs(graph, v, visited, n):
    visited[v] = True
    count = 1

    for i in range(1, n + 1):
        if graph[v][i] == 1 and not visited[i]:
            count += dfs(graph, i, visited, n)
    return count

visited = [False] * (n+1)
result = dfs(graph, 1, visited, n)
print(result-1)