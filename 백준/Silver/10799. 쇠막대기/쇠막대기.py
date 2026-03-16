pipe = input()
stack = []
answer = 0

for i in range(len(pipe)):
    if pipe[i] == "(":
        stack.append("(")
    else:
        stack.pop()
        if pipe[i-1] == "(":
            answer += len(stack)
        else:
            answer += 1

print(answer)