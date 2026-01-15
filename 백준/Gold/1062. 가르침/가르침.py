import sys
from itertools import combinations

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
k = int(input_data[1])

if k < 5:
    print(0)
    exit()

words = []
for j in range(n):
    temp = input_data[j + 2]
    temp = temp[4:-4] 
    words.append(temp)

counts = {}
essential = {'a', 'n', 't', 'i', 'c'}
for w in words:
    for char in w:
        if char not in essential:
            counts[char] = counts.get(char, 0) + 1

candidates = list(counts.keys())
pick = k - 5

if len(candidates) <= pick:
    print(n)
    exit()

ans = 0
for combo in combinations(candidates, pick):
    learned = essential | set(combo)
    current_sum = 0
    for q in words: 
        possible = True
        for i in q: 
            if i not in learned:
                possible = False
                break
        if possible:
            current_sum += 1
    if current_sum > ans:
        ans = current_sum

print(ans)