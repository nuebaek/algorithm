def solution(n, computers):
    def dfs(v):
        visited[v] = True
        for i in range(n):
            if i != v and computers[v][i] == 1 and not visited[i]:
                dfs(i)
    
    visited = [False for _ in range(n)]
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer