from itertools import combinations

l, c = map(int, input().split())
lst = input().split()

lst.sort()

vowels = ['a', 'e', 'i', 'o', 'u']

for i in combinations(lst, l):
    count_v = 0
    for j in i:
        if j in vowels:
            count_v += 1

    # 자음 개수 구하기
    count_c = l - count_v

    # 모음이 1개 이상이고 자음이 2개 이상일 때만 출력
    if count_v >= 1 and count_c >= 2:
        print(''.join(i))