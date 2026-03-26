import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]

dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j] == 1:
            min_vol = j - v[i-1]
            max_vol = j + v[i-1]

            if min_vol >= 0:
                dp[i][min_vol] = 1

            if max_vol <= m:
                dp[i][max_vol] = 1

answer = -1

for i in range(m, -1, -1):
    if dp[n][i] == 1:
        answer = i
        break

print(answer)