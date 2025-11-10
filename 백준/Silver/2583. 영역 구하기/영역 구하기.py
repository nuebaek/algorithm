from collections import deque

m, n, k = map(int, input().split())
nums = []
for _ in range(k):
    a, b, c, d = map(int, input().split())
    nums.append((a, b, c, d))

graph = [[0]*n for _ in range(m)]

for (a, b, c, d) in nums:
    for y in range(b, d):
        for x in range(a, c):
            graph[y][x] = 1

visited = [[False]*n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    size += 1
    return size

blank = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and not visited[i][j]:
            blank.append(bfs(i, j))

blank.sort()
print(len(blank))
print(*blank)