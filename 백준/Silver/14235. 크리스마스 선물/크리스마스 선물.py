import heapq
import sys

input = sys.stdin.readline
n = int(input())

gift = []

for _ in range(n):
    a = list(map(int, input().split()))

    if a[0] == 0:
        if gift:
            print(-heapq.heappop(gift))
        else:
            print(-1)
    else:
        for i in range(1, a[0] + 1):
            heapq.heappush(gift, -a[i])