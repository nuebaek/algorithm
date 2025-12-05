from itertools import permutations
n = int(input())
a = list(map(int, input().split()))

answer = 0

for p in permutations(a, n):
    current = 0
    for i in range(n-1):
        current += abs(p[i]-p[i+1])
    answer = max(answer, current)

print(answer)