import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    dp = [list(map(int,input().split())) for _ in range(2)]

    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for k in range(2, n):
        dp[0][k] += max(dp[1][k-1], dp[1][k-2])
        dp[1][k] += max(dp[0][k-1], dp[0][k-2])

    print(max(dp[0][n-1], dp[1][n-1]))