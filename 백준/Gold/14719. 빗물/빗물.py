import sys
input = sys.stdin.readline

h, w = map(int, input().split())
height = list(map(int, input().split()))

volume = 0
left, right = 0, w-1
left_max, right_max = height[left], height[right]

while left < right:
    left_max = max(height[left], left_max) 
    right_max = max(height[right], right_max)
    
    if left_max <= right_max:
        volume += left_max - height[left]
        left += 1
        
    else:
        volume += right_max - height[right]
        right -= 1

print(volume)