import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[[-1] * 3 for _ in range(n)] for _ in range(n)]

def dfs(r, c, shape):
    if r == n-1 and c == n-1:
        return 1

    if dp[r][c][shape] != -1:
        return dp[r][c][shape]

    count = 0
    
    # 가로 이동
    if shape == 0 or shape == 2:
        if c + 1 < n and grid[r][c+1] == 0:
            count += dfs(r, c+1, 0)
            
    # 세로 이동
    if shape == 1 or shape == 2:
        if r + 1 < n and grid[r+1][c] == 0:
            count += dfs(r+1, c, 1)
            
    # 대각선 이동 
    if r + 1 < n and c + 1 < n:
        if grid[r+1][c] == 0 and grid[r][c+1] == 0 and grid[r+1][c+1] == 0:
            count += dfs(r+1, c+1, 2)

    dp[r][c][shape] = count
    return count

print(dfs(0, 1, 0))