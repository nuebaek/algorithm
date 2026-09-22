from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for order in permutations(dungeons):
        energy = k
        count = 0

        for required, cost in order:
            if energy < required:
                break

            energy -= cost
            count += 1

        answer = max(answer, count)

    return answer


# 1. 던전을 갈 수 있는 모든 순서로 나열한다.
# 2. 각 순서대로 앞에서부터 실제로 탐험한다.
# 3. 피로도가 부족하면 그 순서는 중단한다.
# 4. 가장 많이 탐험한 횟수를 반환한다.
