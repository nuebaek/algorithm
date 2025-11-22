n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]
score.insert(0, [0, 0, 0])

d = [[0]*3 for _ in range(n+1)]

d[1][0], d[1][1], d[1][2] = score[1][0], score[1][1], score[1][2]

for i in range(2, n+1):
    # 빨간색으로 칠했을 때
    d[i][0] = min(d[i-1][1], d[i-1][2]) + score[i][0]
    # 초록색으로 칠했을 때
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + score[i][1]
    # 파란색으로 칠했을 때
    d[i][2] = min(d[i - 1][1], d[i - 1][0]) + score[i][2]

print(min(d[n]))