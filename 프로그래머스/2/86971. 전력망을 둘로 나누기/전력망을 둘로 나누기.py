from collections import deque

def bfs(start, visited, graph):
    cnt = 1
    q = deque([start])
    visited[start] = True
    
    while q:
        v = q.popleft()
        
        for i in graph[v]:
            if visited[i]:
                continue
                
            q.append(i)
            cnt += 1
            visited[i] = True
    return cnt


def solution(n, wires):
    answer = n
    
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for start, split, in wires:
        visited = [False] * (n+1)
        visited[split] = True
        cnt = bfs(start, visited, graph)
        if abs(cnt-(n-cnt)) < answer:
            answer = abs(cnt-(n-cnt))
        
    return answer
