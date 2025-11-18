n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]

board = [[0]*100 for _ in range(100)] 

for x, y in papers:
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1  

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            answer += 1

print(answer)