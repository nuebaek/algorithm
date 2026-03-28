t = int(input())
length = [int(input()) for _ in range(t)]

max_val = max(length)
dp = [0] * (max_val + 1)

dp[0] = 1
if max_val >= 2:
    dp[2] = 1

for i in range(4, max_val+1, 2):
    for j in range(2, i+1, 2):
        dp[i] += (dp[j-2] * dp[i-j])
        dp[i] %= 1000000007

for i in length:
    if i % 2 == 1:
        print(0)
    else:
        print(dp[i])