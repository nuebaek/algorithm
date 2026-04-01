import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    heapq.heappush(heap, int(input()))

if n == 1:
    print(0)
    sys.exit()

total_cost = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    
    sum_value = a + b
    total_cost += sum_value
    
    heapq.heappush(heap, sum_value)

print(total_cost)