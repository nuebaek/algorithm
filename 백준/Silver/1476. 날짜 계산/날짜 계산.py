E, S, M = map(int, input().split())

count = 1

while True:
    # count 값으로 e, s, m을 계산해서 E, S, M과 일치하는지 확인
    if (count - 1) % 15 + 1 == E and \
            (count - 1) % 28 + 1 == S and \
            (count - 1) % 19 + 1 == M:
        break

    count += 1

print(count)