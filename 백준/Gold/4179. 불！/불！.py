import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

fire_q = deque()
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist_fire = [[-1] * c for _ in range(r)]
dist_j = [[-1] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            fire_q.append((i, j))
            dist_fire[i][j] = 0
        elif graph[i][j] == 'J':
            q.append((i, j))
            dist_j[i][j] = 0

while fire_q:
    x, y = fire_q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] != '#' and dist_fire[nx][ny] == -1:
                dist_fire[nx][ny] = dist_fire[x][y] + 1
                fire_q.append((nx, ny))

while q:
    x, y = q.popleft()
    if x == 0 or x == r - 1 or y == 0 or y == c - 1:
        print(dist_j[x][y] + 1)
        break

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] == '#':
                continue
            if dist_j[nx][ny] != -1:
                continue
            next_time = dist_j[x][y] + 1
            if dist_fire[nx][ny] != -1 and dist_fire[nx][ny] <= next_time:
                continue
            dist_j[nx][ny] = next_time
            q.append((nx, ny))
else:
    print("IMPOSSIBLE")