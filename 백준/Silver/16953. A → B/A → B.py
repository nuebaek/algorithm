import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())

q = deque([(a, 1)])

while q:
    x, c = q.popleft()
    if x == b:
        print(c)
        exit()
    if x*2 <= b:
        q.append((x*2, c+1))
    if x*10+1 <= b:
        q.append((x*10+1, c+1))
print(-1)