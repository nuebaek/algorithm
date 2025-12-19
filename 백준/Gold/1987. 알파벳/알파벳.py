import sys

def solve():
    r, c = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(r)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = set([(0, 0, board[0][0])])
    max_dist = 0

    while queue:
        x, y, path = queue.pop()
        max_dist = max(max_dist, len(path))
        
        if max_dist == 26:
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] not in path:
                    queue.add((nx, ny, path + board[nx][ny]))

    print(max_dist)

solve()