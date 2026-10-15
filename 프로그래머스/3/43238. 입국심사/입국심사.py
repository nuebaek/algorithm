def solution(n, times):
    left = 1
    right = min(times) * n

    while left < right:
        middle = (left + right) // 2

        
        checked = 0
        for time in times:
            checked += middle // time
            
        if checked >= n:
            right = middle
            
        else:
            left = middle + 1

    return left


# 1분부터 가장 빠른 심사관이 혼자 전부 심사하는 시간까지를 범위로 설정
# 범위의 가운데 시간 고름(이분탐색)
# 그 시간 동안 모든 심사관이 심사할 수 있는 사람 수를 더하고
# n명 이상이면 더 짧은 시간도 가능한지 확인
# n명 미만이면 시간이 부족하므로 시간 추가해서 확인
# left == right가 되면 정답