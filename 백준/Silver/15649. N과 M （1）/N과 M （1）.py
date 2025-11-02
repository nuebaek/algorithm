n, m = map(int, input().split())
ans = []
v = [0]*(n+1)

def dfs(i, k):
    if i == m:
        ans.append(k)
        return
    for j in range(1, n+1):
        if v[j] == 0:
            v[j] = 1
            dfs(i+1, k+[j])
            v[j]=0

dfs(0, [])
for k in ans:
    print(*k)