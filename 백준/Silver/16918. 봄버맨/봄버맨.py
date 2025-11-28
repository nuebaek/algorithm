from collections import deque

r, c, n = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# n == 1 : 처음 상태 그대로
if n == 1:
    for g in graph:
        print(''.join(g))

# n이 짝수면 항상 전체 폭탄
elif n % 2 == 0:
    for _ in range(r):
        print('O' * c)

# 그 외 (n >= 3 이고 홀수인 경우)
else:
    def explode(board):
        full = [['O'] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    # 해당 폭탄 위치
                    full[i][j] = '.'
                    # 상하좌우도 함께 파괴
                    for k in range(4):
                        ni = i + dx[k]
                        nj = j + dy[k]
                        if 0 <= ni < r and 0 <= nj < c:
                            full[ni][nj] = '.'
        return full

    first = explode(graph)       
    second = explode(first)     

    if n % 4 == 3:
        result = first
    else:  
        result = second

    for row in result:
        print(''.join(row))