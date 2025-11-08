from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

count = 0
answer = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    a = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                a += 1
                queue.append((nx, ny))
    return a

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count += 1
            answer = max(answer, bfs(i, j))

print(count)
print(answer)