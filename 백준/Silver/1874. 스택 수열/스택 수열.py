n = int(input())
target = [int(input()) for _ in range(n)]

stack = []
answer = []
current = 1
find = True

for t in target:
    while current <= t:
        stack.append(current)
        answer.append('+')
        current += 1

    if stack[-1] == t:
        stack.pop()
        answer.append('-')
    else:
        find = False
        break

if find:
    for a in answer:
        print(a)
else:
    print("NO")