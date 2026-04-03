n = int(input())
target = int(input())
arr = [[-1] * n for _ in range(n)]

cur_num = n * n
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 하, 우, 상, 좌
idx = 0
cx, cy = 0, 0
ax, ay = 0, 0 

while cur_num > 0:
    arr[cy][cx] = cur_num
    if cur_num == target:
        ax, ay = cx + 1, cy + 1
        
    cur_num -= 1
    if cur_num == 0: 
        break 
        
    nx, ny = cx + dx[idx], cy + dy[idx]
    
    if not (0 <= nx < n and 0 <= ny < n and arr[ny][nx] == -1):
        idx = (idx + 1) % 4
        nx, ny = cx + dx[idx], cy + dy[idx]
        
    cx, cy = nx, ny

for row in arr:
    print(*row) 

print(ay, ax)