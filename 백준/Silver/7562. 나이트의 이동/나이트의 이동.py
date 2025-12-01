from collections import deque

t = int(input())
l = []
board = []
for i in range(t):
    l.append(int(input()))
    element = [list(map(int, input().split())) for _ in range(2)]
    board.append(element)

# 나이트가 한 번에 이동할 수 있는 칸
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(n, s, e):
    q = deque()
    graph = [[0]*n for _ in range(n)]
    q.append(s)

    if s == e:
        return print(0)

    while q:
        num = q.popleft()
        x, y = num[0], num[1]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0 <=ny<n:
                if nx == e[0] and ny == e[1]:
                    graph[nx][ny] = graph[x][y] + 1
                    return print(graph[nx][ny])
                elif graph[nx][ny]==0:
                    q.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1
                else:
                    continue

for i in range(t):
    bfs(l[i], board[i][0], board[i][1])