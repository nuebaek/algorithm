n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p = sorted(range(n), key=lambda i: b[i], reverse=True)
a.sort()

a_sort = [0] * n
for i in range(n):
    a_sort[p[i]] = a[i]
a = a_sort

answer = 0
for i in range(n):
    answer += a[i] * b[i]

print(answer)