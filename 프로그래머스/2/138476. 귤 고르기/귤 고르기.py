def solution(k, tangerine):
    tangerine.sort()
    counts = []
    previous = None
    types = 0
    answer = 0

    for t in tangerine:
        if t == previous:
            counts[-1] += 1
        else:
            previous = t
            counts.append(1)
    
    counts.sort(reverse=True)
    i = 0
    
    while types < k:
        types += counts[i]
        answer += 1
        i += 1
        
    return answer
    

# 1. 사이즈 별로 개수를 count
# 2. 개수(counts)를 내림차순 정렬
# 3. 개수(counts)를 순차적으로 더하면서, 현재 개수가 k와 같거나 크면 종류에 값을 더하는 것을 멈춘다