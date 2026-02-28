import sys
input = sys.stdin.readline

n = int(input())
t, p = [0], [0]
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0]*(n+1)

for i in range(1, n+1):
    dp[i] = max(dp[i], dp[i-1])
    d = i+t[i]-1
    if d <= n:
        dp[d] = max(dp[d], dp[i-1] + p[i])

print(max(dp))