def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    
    while left < right:
        level = (left + right) // 2
        
        running_time = 0
        for i in range(len(diffs)):
            if level >= diffs[i]:
                running_time += times[i]
            
            else: 
                incorrect = diffs[i] - level
                time_cur = times[i]
                time_prev = 0
                
                if i > 0:
                    time_prev = times[i-1]
                    
                res = (time_prev + time_cur) * (incorrect) + time_cur
                running_time += res
                
        if running_time <= limit:
            right = level
            
        else:
            left = level + 1
        
    return left


# 숙련도 1부터 가장 높은 퍼즐 난이도까지를 범위로 설정
# 범위의 가운데 숙련도를 고름
# 그 숙련도로 모든 퍼즐을 푸는 데 걸리는 시간을 계산
# 총 시간이 제한 시간 이하이면 더 낮은 숙련도도 가능한지 확인
# 총 시간이 제한 시간보다 크면 숙련도를 높인다
# left == right가 되면 정답
