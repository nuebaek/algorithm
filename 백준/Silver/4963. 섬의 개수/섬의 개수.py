import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(start_y, start_x):
    queue = deque([(start_y, start_x)])
    graph[start_y][start_x] = 0 

    while queue:
        y, x = queue.popleft()

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < h and 0 <= nx < w and graph[ny][nx] == 1:
                graph[ny][nx] = 0  
                queue.append((ny, nx))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
        
    graph = [list(map(int, input().split())) for _ in range(h)]
    ans = 0

    for i in range(h): 
        for j in range(w): 
            if graph[i][j] == 1: 
                bfs(i, j)        
                ans += 1        

    print(ans)