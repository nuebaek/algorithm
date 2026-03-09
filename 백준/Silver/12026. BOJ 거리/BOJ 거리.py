import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().strip()) 

d = [float('inf')] * n
d[0] = 0

for i in range(n):
    for j in range(i):
        if d[j] == float('inf'):
            continue
            
        if arr[i] == 'B' and arr[j] == 'J':
            d[i] = min(d[i], d[j]+(i-j)*(i-j))
        if arr[i] == 'O' and arr[j] == 'B':
            d[i] = min(d[i], d[j]+(i-j)*(i-j))
        if arr[i] == 'J' and arr[j] == 'O':
            d[i] = min(d[i], d[j]+(i-j)*(i-j))

if d[-1] == float('inf'):
    print(-1)
else:
    print(d[-1])