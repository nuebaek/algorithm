from collections import deque
n, k = map(int, input().split())

def bfs(n, k):
    v = [-1] * 100001
    queue = deque([n])
    v[n] = 0
    
    min_time = 0
    ways = 0
    
    while queue:
        cur = queue.popleft()
        
        if cur == k:
            min_time = v[cur]
            ways += 1
            continue 

        for nxt in (cur-1, cur+1, cur*2):
            if 0 <= nxt < 100001:
                if v[nxt] == -1:
                    v[nxt] = v[cur] + 1
                    queue.append(nxt)
                
                elif v[nxt] == v[cur] + 1:
                    queue.append(nxt)
                    
    return min_time, ways

time, count = bfs(n, k)
print(time)
print(count)