n = int(input())
x, y = map(int, input().split())
m = int(input())
graph = [[]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(x, y, visited):
    if x == y:
        return 0

    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            res = dfs(i, y, visited)
            if res != -1:
                return res + 1
    return -1

print(dfs(x, y, visited))