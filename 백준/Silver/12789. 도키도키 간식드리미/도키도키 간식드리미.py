import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
stack = []
need = 1

for i in a:
    if i == need:
        need += 1
    else:
        stack.append(i)
    while stack and stack[-1] == need:
        stack.pop()
        need += 1

if need == n+1:
    print("Nice")
else:
    print("Sad")