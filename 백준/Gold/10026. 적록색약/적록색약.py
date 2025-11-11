import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

graph2 = [['R' if ch in ('R', 'G') else 'B' for ch in row] for row in graph]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, color, g, vis):
    vis[x][y] = True
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if not vis[nx][ny] and g[nx][ny] == color:
                dfs(nx, ny, color, g, vis)

def count_components(g):
    vis = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not vis[i][j]:
                cnt += 1
                dfs(i, j, g[i][j], g, vis)
    return cnt

rgb = count_components(graph)   # 일반 시야
rb  = count_components(graph2)  # 적록색약 시야

print(rgb, rb)