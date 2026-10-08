def solution(N, number):
    dp = [set() for _ in range(9)]

    for k in range(1, 9):
        dp[k].add(int(str(N) * k))

        for i in range(1, k):
            for a in dp[i]:
                for b in dp[k - i]:
                    dp[k].update((a + b, a - b, a * b))
                    if b != 0:
                        dp[k].add(int(a / b))

        if number in dp[k]:
            return k

    return -1



# k의 개수를 기준으로 점화식을 세운다
# dp[1] 은 N을 1개 써서 만들 수 있는 값들의 집합
# dp[3]은 dp[1], [2]의 값들을 사칙연산한 값, NNN이 포함될 것
