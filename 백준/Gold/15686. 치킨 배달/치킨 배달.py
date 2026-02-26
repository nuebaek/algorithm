import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
result = 100001
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])

for c in combinations(chicken, m):
    temp = 0
    for h in house:
        dist = 100001
        for j in range(m):
            dist = min(dist, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
        temp += dist
    result = min(result, temp)

print(result)