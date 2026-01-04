import sys

input = sys.stdin.readline
n = int(input())
board = [list(input()) for _ in range(n)]
answer = 1

def check():
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
    return max_cnt

for i in range(n):
    for j in range(n - 1):
        # 가로
        if j + 1 < n and board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            answer = max(answer, check())
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        # 세로
        if i + 1 < n and board[i][j] != board[i + 1][j]:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            answer = max(answer, check())
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(answer)