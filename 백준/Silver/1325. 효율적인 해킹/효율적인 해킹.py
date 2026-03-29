import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start, n, graph):
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True
    cnt = 1

    while q:
        curr = q.popleft()
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                cnt += 1

    return cnt

max_cnt = 0
ans = []

for i in range(1, n + 1):
    if not graph[i]:
        curr_cnt = 1
    else:
        curr_cnt = bfs(i, n, graph)

    if curr_cnt > max_cnt:
        max_cnt = curr_cnt
        ans = [i]
    elif curr_cnt == max_cnt:
        ans.append(i)

print(*(ans))