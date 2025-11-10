from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

v = [[0]*n for _ in range(m)]

queue = deque()

result, answer = 0, 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and graph[nx][ny]==0:
            graph[nx][ny] = 1
            v[nx][ny] = v[x][y]+1
            queue.append((nx, ny))

check = False
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            check = True
if check:
    print(-1)
else:
    answer = 0
    for i in range(m):
        for j in range(n):
            answer = max(answer, v[i][j])
    print(answer)