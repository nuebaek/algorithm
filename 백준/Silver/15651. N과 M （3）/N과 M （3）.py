n, m = map(int, input().split())
nums = [str(i) for i in range(1, n + 1)]

result = []

def dfs(depth):
    if depth == m:
        print(' '.join(result))
        return
    for num in nums:
        result.append(num)
        dfs(depth + 1)
        result.pop()

dfs(0)