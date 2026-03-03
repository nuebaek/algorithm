import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truth = set(list(map(int, input().split()))[1:])
parties = [set(list(map(int, input().split()))[1:]) for _ in range(m)]

for _ in range(m):
    for party in parties:
        if party & truth: 
            truth = truth.union(party)

ans = 0
for party in parties:
    if not (party & truth):
        ans += 1

print(ans)