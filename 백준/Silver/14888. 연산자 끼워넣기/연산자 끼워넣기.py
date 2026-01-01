import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

# 최댓값, 최솟값 초기화
max_val = -float('inf')
min_val = float('inf')

def dfs(idx, current_total, p, m, mu, d):
    global max_val, min_val

    if idx == n:
        max_val = max(max_val, current_total)
        min_val = min(min_val, current_total)
        return

    if p > 0:
        dfs(idx + 1, current_total + nums[idx], p - 1, m, mu, d)
    if m > 0:
        dfs(idx + 1, current_total - nums[idx], p, m - 1, mu, d)
    if mu > 0:
        dfs(idx + 1, current_total * nums[idx], p, m, mu - 1, d)
    if d > 0:
        dfs(idx + 1, int(current_total / nums[idx]), p, m, mu, d - 1)

dfs(1, nums[0], plus, minus, mul, div)

print(max_val)
print(min_val)