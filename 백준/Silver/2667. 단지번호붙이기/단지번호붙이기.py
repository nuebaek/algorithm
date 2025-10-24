n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * (n) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    size = 1
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                size += dfs(nx, ny)
    return size

danji = 0
house_cnt = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            danji += 1
            house_cnt.append(dfs(i, j))

print(danji)
house_cnt.sort()
for x in house_cnt:
    print(x, end="\n")