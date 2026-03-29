import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)

    def bfs(start):
        q = deque([start])
        visited = [False] * (n + 1)
        visited[start] = True
        cnt = 1
        while q:
            curr = q.popleft()
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    cnt += 1
                    q.append(neighbor)
        return cnt

    max_cnt = 0
    ans = []

    for i in range(1, n + 1):
        if not graph[i]:
            curr_cnt = 1
        else:
            curr_cnt = bfs(i)
        
        if curr_cnt > max_cnt:
            max_cnt = curr_cnt
            ans = [i]
        elif curr_cnt == max_cnt:
            ans.append(i)

    print(*(ans))

solve()