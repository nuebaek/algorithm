from itertools import combinations
n, m = map(int, input().split())

nums=""
for i in range(1, n+1):
    nums += str(i)

for i in combinations(nums, m):
    print(*i)