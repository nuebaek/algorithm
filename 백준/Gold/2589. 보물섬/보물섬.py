from collections import deque

n, m = map(int, input().split())
treasure = [list(input()) for _ in range(n)]

land = []
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# land 좌표 찾기
for i in range(n):
    for j in range(m):
        if  treasure[i][j] == "L":
            land.append([i, j])
        else:
            continue


# bfs 구조 작성
def bfs(x, y):
    q = deque()
    q.append([x, y])
    graph = [[0] * m for _ in range(n)]
    graph[x][y] = 1
    time = 0

    while q:
        [x, y] = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if treasure[nx][ny] == "L" and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])
                    time += 1

    return max(map(max, graph)) - 1


# 메인 루프
for i in land:
    cur = bfs(i[0], i[1])
    ans = max(ans, cur)

print(ans)