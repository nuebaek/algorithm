import math

def solution(progresses, speeds):
    answer = []
    counts = []
    
    for i in range(len(progresses)):
        res = math.ceil((100-progresses[i])/speeds[i])
        counts.append(res)
        
            
    day = counts[0]
    for i in range(len(counts)): 
        if i == 0:
            answer.append(1)
        else:
            if counts[i] <= day:
                answer[-1] += 1
            else:
                answer.append(1)
                day = counts[i]

    return answer