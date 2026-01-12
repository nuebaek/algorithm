import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(m)]

visited = [[False] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, color):
    visited[x][y] = True
    size = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if graph[nx][ny] == color and not visited[nx][ny]:
                size += dfs(nx, ny, color)
    return size

total_w, total_b = 0, 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] == "W":
                total_w += dfs(i, j, "W") ** 2
            else:
                total_b += dfs(i, j, "B") ** 2

print(total_w, total_b)