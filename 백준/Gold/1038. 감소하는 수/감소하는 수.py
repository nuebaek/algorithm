from itertools import combinations

n = int(input())

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = []

for i in range(1, 11):
    for j in combinations(lst, i):
        temp = list(j)
        temp.sort(reverse=True)
        answer.append(int("".join(map(str, temp))))

answer.sort()

if n >= len(answer):
    print(-1)
else:
    print(answer[n])