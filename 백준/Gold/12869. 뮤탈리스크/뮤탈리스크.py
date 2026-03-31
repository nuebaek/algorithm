from itertools import permutations

n = int(input())

scv = list(map(int, input().split()))

if n == 1:
    scv = scv + [0,0]
elif n == 2:
    scv = scv + [0]

dp=[[[1000 for _ in range(61)]for _ in range(61)]for _ in range(61)]

def dfs(x,y,z):
    if x <= 0 and y <= 0 and z <= 0:
        return 0

    if x < 0: x = 0
    if y < 0: y = 0
    if z < 0: z = 0

    if dp[x][y][z] < 1000: return dp[x][y][z]

    for i,j,k in list(permutations([9,3,1])):
        dp[x][y][z] = min(dp[x][y][z], dfs(x - i, y - j, z - k) + 1)

    return dp[x][y][z]

print(dfs(scv[0],scv[1],scv[2]))