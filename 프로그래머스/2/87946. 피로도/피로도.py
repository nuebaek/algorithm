def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = 0
    
    
    def dfs(need, count):
        nonlocal answer
        if count > answer:
            answer = count
          
        for i in range(len(dungeons)):
            min_needed, cost = dungeons[i] 
            if not visited[i] and need >= min_needed:
                visited[i] = True
                dfs(need-cost, count+1)
                visited[i] = False
                
    dfs(k, 0)
    return answer