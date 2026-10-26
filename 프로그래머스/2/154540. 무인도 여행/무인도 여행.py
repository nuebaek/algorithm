import sys
sys.setrecursionlimit(100000)

def solution(maps):
    r, c = len(maps), len(maps[0])
    visited = [[False]*(c) for _ in range(r)]
    answer = []
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    def dfs(y, x, visited, value):
        visited[y][x] = True
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
        
            if (0<=ny<r and 0<=nx<c):
                if maps[ny][nx] != "X":
                    if not visited[ny][nx]:
                        value += int(maps[ny][nx])
                        value = dfs(ny, nx, visited, value)
                
        return value
    
    for i in range(r):
        for j in range(c):
            if maps[i][j] != "X" and not visited[i][j]:
                value = int(maps[i][j])  
                value = dfs(i, j, visited, value) 
                answer.append(value)
    
    if len(answer)>0:
        answer.sort()
        return answer
    
    else:
        return [-1]
    