N, S = map(int, input().split())
lst = list(map(int, input().split()))

answer = 0

def dfs(n, sum, count):
    global answer
    if n==N:
        if sum == S and count > 0:
            answer += 1
        return

    # 포함/미포함 경우 나누어 dfs 재귀 호출
    dfs(n+1, sum+lst[n], count+1)
    dfs(n+1, sum, count)

dfs(0, 0, 0)
print(answer)