from collections import deque

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, graph):
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <=nx<M and 0<=ny<N and graph[nx][ny]==1:
                queue.append([nx, ny])
                graph[nx][ny] = 0

for _ in range(T):
    M, N, K = map(int, input().split()) 
    graph = [[0]*N for _ in range(M)]   
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    count = 0
    for j in range(M):
        for k in range(N):
            if graph[j][k] == 1:
                bfs(j, k, graph)
                count += 1
    print(count)