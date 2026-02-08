n, r, c = map(int, input().split())

def solve():
    global n, r, c
    answer = 0

    while n != 0:
        n -= 1
        half = 2 ** n

        if r < half and c < half:
            answer += 0

        elif r < half and c >= half:
            answer += half * half
            c -= half

        elif r >= half and c < half:
            answer += half * half * 2
            r -= half

        else:
            answer += half * half * 3
            r -= half
            c -= half

    print(answer)

solve()