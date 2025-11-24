n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def dfs(d, current_profit):
    global answer

    if d == n:
        answer = max(answer, current_profit)
        return

    if d > n:
        return

    # 퇴사일 넘기지 않으면 오늘 상담
    if d + p[d][0] <= n:
        dfs(d+p[d][0], current_profit+p[d][1])

    # 다음날로 넘김
    dfs(d+1, current_profit)

dfs(0, 0)
print(answer)