n = int(input())
dp = [0] * n
wine = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(wine))

else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = sum(wine[:3]) - min(wine[:3])

    for i in range(3, n):
        # 1. 이번 잔 안 마심 (dp[i-1])
        # 2. 직전 잔 안 마시고 이번 잔 마심 (dp[i-2] + wine[i])
        # 3. 직전 잔 마시고 이번 잔 마심 (dp[i-3] + wine[i-1] + wine[i])
        dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])

    print(dp[-1])