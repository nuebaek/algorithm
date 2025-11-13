from itertools import product

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

for i in product(nums, repeat=m):
    print(*i)