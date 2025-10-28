from collections import deque
n, k = map(int, input().split())

def bfs(s, e):
    queue = deque([])
    v = [0]*100001

    queue.append(s)
    v[s] = 1

    while queue:
        cur = queue.popleft()
        if cur == e:
            return v[e]-1

        for n in (cur-1, cur+1, cur*2):
            if 0<=n<100001 and v[n]==0:
                queue.append(n)
                v[n] = v[cur] + 1

result = bfs(n, k)
print(result)