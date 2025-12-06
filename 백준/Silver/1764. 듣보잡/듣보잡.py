import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = set(input().strip() for _ in range(n))

lst = []
answer = 0

for _ in range(m):
    word = input().strip()
    if word in l:
        answer += 1
        lst.append(word)

lst.sort()

print(answer)
for i in lst:
    print(i)