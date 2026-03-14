import sys
input = sys.stdin.readline

h, w = map(int, input().split())
height = list(map(int, input().split()))

stack = []
volume = 0

for i in range(w):
    while stack and height[i] > height[stack[-1]]:
        top = stack.pop()

        if not len(stack):
            break

        distance = i - stack[-1] - 1
        waters = min(height[i], height[stack[-1]]) - height[top]

        volume += distance * waters

    stack.append(i)
print(volume)