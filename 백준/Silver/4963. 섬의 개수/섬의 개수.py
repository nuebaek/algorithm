import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(start_x, start_y):
    # if 0 <= i < h and 0 <= j < w :
    if start_x < 0 or start_x >= h or start_y < 0 or start_y >= w or graph[start_x][start_y] != 1:
        return

    graph[start_x][start_y] = 0

    for i in range(8):
        nx = start_x + dx[i]
        ny = start_y + dy[i]

        dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                ans += 1

    print(ans)