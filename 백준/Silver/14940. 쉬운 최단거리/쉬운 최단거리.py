from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]

            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == -1 and graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])

# 목표 좌표 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            a, b = i, j
        else:
            continue

start_x, start_y = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i, j
        elif graph[i][j] == 0:
            visited[i][j] = 0

bfs(start_x, start_y)

for row in visited:
    print(*row)