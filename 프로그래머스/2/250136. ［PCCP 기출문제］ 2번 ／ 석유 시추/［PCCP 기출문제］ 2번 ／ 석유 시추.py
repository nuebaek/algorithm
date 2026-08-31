from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[False] * m for _ in range(n)]
    oil = [0] * m  
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                oil_size = 0
                cols = set()
                
                while queue:
                    x, y = queue.popleft()
                    oil_size += 1
                    cols.add(y)
                    
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                
                for col in cols:
                    oil[col] += oil_size
                    
    return max(oil)
