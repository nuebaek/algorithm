# 인접 행렬
# from collections import deque
#
# n, m, v = map(int, input().split())
# graph = [[0]*(n+1) for _ in range(n+1)]
# for i in range(m):
#     x, y = map(int, input().split())
#     graph[x][y] = graph[y][x] = 1
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=" ")
#
#     for i in range(1, n+1):
#         if graph[v][i] ==1 and not visited[i]:
#             dfs(graph, i, visited)
#
# def bfs(graph, v, visited):
#     queue = deque([v])
#     visited[v] = True
#
#     while queue:
#         v = queue.popleft()
#         print(v, end=" ")
#         for i in range(1, n+1):
#             if graph[v][i] == 1 and not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
#
#
# visited1 = [False] * (n+1)
# visited2 = [False] * (n+1)
#
# dfs(graph, v, visited1)
# print()
# bfs(graph, v, visited2)


# 인접 리스트
from collections import deque

n, m, v = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)