from collections import deque
import sys
input = sys.stdin.readline

coin = []
board = []

n, m = map(int, input().split())
for i in range(n):
    temp = list(input().strip())
    board.append(temp)

    for j, val in enumerate(temp):
        if val == 'o':
            coin.append([i, j])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    queue = deque([(coin[0][0], coin[0][1], coin[1][0], coin[1][1], 0)])

    while queue:
        cur = queue.popleft() 
        
        if cur[4] >= 10:
            continue

        for k in range(4):
            ny1 = cur[0] + dy[k]
            nx1 = cur[1] + dx[k]
            ny2 = cur[2] + dy[k]
            nx2 = cur[3] + dx[k]

            # 동전 1이 떨어졌을 때
            if ny1 < 0 or ny1 >= n or nx1 < 0 or nx1 >= m:
                # 동전 2도 떨어졌을 때 > 실패
                if ny2 < 0 or ny2 >= n or nx2 < 0 or nx2 >= m:
                    continue
                # 동전 1만 떨어졌을 때 > 정답
                else:
                    return cur[4] + 1
                    
            # 동전 2만 떨어졌을 때 > 정답
            elif ny2 < 0 or ny2 >= n or nx2 < 0 or nx2 >= m:
                return cur[4] + 1

            # 둘 다 안 떨어졌을 때
            else:
                # 벽
                if board[ny1][nx1] == "#":
                    ny1, nx1 = cur[0], cur[1]
                if board[ny2][nx2] == "#":
                    ny2, nx2 = cur[2], cur[3]

                queue.append((ny1, nx1, ny2, nx2, cur[4] + 1))

    return -1

print(bfs())