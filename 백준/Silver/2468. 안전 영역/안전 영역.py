import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, s, visited):
    visited[x][y] = True
    size = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and graph[nx][ny] > s:
                size = size + dfs(nx, ny, s, visited)
    return size

answer = 0
height = max(map(max, graph))

for h in range(0, height+1):
    visited = [[False] * (n) for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]:
                dfs(i, j, h, visited)
                count += 1
    answer = max(answer, count)

print(answer)