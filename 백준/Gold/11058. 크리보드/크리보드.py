n = int(input())

dp = [0]*(n+1)

for i in range(n+1):
    if i < 6:
        dp[i] = i
    else:
        dp[i] = max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)

print(dp[n])