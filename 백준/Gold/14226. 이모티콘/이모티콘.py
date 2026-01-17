
from collections import deque

ans = int(input())

visited = [[-1] * 1001 for _ in range(1001)]

def solve():
    q = deque([(1, 0)])
    visited[1][0] = 0

    while q:
        s, c = q.popleft()

        if s == ans:
            print(visited[s][c])
            return

        if visited[s][s] == -1:
            visited[s][s] = visited[s][c] + 1
            q.append((s, s))

        if s + c <= 1000 and visited[s + c][c] == -1:
            visited[s + c][c] = visited[s][c] + 1
            q.append((s + c, c))

        if s - 1 >= 0 and visited[s - 1][c] == -1:
            visited[s - 1][c] = visited[s][c] + 1
            q.append((s - 1, c))

solve()