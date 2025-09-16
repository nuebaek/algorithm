import math
def solution(progresses, speeds):
    answer = []
    counts = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    while counts:
        day = counts[0]
        cnt = 0
        while counts and counts[0] <= day:
            cnt += 1
            counts.pop(0)
        answer.append(cnt)
    return answer


#  올림, 내림 > math.ceil(), math.floor()
#  반올림 > round()