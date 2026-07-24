from collections import deque

def bfs(graph):
    start_y, start_x = 0, 0
    q = deque([(start_y, start_x)])
    
    m = len(graph)
    n = len(graph[0])
    
    visited = [[False]*(n) for _ in range(m)]
    visited[start_y][start_x] = True
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < m and 0 <= nx < n:
                if not visited[ny][nx]:
                     if graph[ny][nx] == 1:
                        visited[ny][nx] = True
                        graph[ny][nx] = graph[y][x] + 1
                        q.append((ny, nx))

    return -1 if graph[m-1][n-1] <= 1 else graph[m-1][n-1]
                        

def solution(maps):
    return bfs(maps)
