
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = list(set(int(input()) for _ in range(n)))

inf = 10001
dp = [inf] * (k + 1)
dp[0] = 0  

for coin in coins:
    for i in range(coin, k + 1):
        if dp[i - coin] != inf:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == inf:
    print(-1)
else:
    print(dp[k])