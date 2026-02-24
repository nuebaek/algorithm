import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [float('inf')] * (V+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        dis, cur = heapq.heappop(q)

        if dist[cur] < dis:
            continue

        for i in graph[cur]:
            cost = dis + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for j in range(1, V+1):
    if dist[j] == float('inf'):
        print("INF")
    else:
        print(dist[j])