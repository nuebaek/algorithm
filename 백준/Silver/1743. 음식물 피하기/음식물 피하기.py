import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    size = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                size += dfs(nx, ny)
    return size

lst = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            lst.append(dfs(i, j))

print(max(lst))