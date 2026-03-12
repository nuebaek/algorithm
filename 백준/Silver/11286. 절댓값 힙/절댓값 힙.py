import heapq
import sys
input = sys.stdin.readline

arr = []

n = int(input())
for _ in range(n):
    num = int(input())
    
    if num == 0:
        if not arr: 
            print(0)
        else:
            print(heapq.heappop(arr)[1])
            
    else:
        heapq.heappush(arr, (abs(num), num))