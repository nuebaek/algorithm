from collections import deque

n, m = map(int, input().split())
graph = [list(map(int,input())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

queue = deque([(0, 0)])
visited = [[False]*(m+1) for _ in range(n+1)]

while queue:
    y, x = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue

        if graph[ny][nx] == 1:
            graph[ny][nx] = graph[y][x] + 1
            queue.append((ny, nx))

print(graph[n-1][m-1])