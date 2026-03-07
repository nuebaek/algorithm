import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

def dfs(start, distance):
    for i, d in graph[start]:
        if visited[i] == -1:
            visited[i] = distance + d
            dfs(i, distance + d)

visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)

max_dist = visited.index(max(visited))
visited = [-1] * (n+1)
visited[max_dist] = 0
dfs(max_dist, 0)

print(max(visited))