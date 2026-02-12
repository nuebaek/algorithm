from collections import deque
n, k = map(int, input().split())

def bfs(s, e):
    queue = deque([s])
    v = [-1]*100001
    v[s] = 0 

    while queue:
        cur = queue.popleft()

        if cur == e:
            return v[e]

        target = cur*2
        if 0 <= target < 100001 and v[target] == -1:
            v[target] = v[cur]
            queue.appendleft(target)

        for nx in (cur-1, cur+1):
            if 0 <= nx < 100001 and v[nx] == -1:
                v[nx] = v[cur] + 1
                queue.append(nx)

result = bfs(n, k)
print(result)