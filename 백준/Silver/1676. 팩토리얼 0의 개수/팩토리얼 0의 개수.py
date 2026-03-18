n = int(input())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

num = str(factorial(n))
answer = 0

for i in range(len(num)-1, -1, -1):
    if num[i] == '0':
        answer += 1
    else:
        break

print(answer)