def solution(people, limit):
    people.sort()
    light = 0
    heavy = len(people)-1
    answer = 0
    
    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
        answer += 1
        
    return answer


# 1. 모든 사람을 구출할 때 필요한 배의 수를 최대한 줄이기
# 2. 한 배에는 최대 두 명까지 탈 수 있고, 두 사람의 무게 합이 limit을 넘으면 안 됨
# 3. 가장 무거운 사람을 기준 가장 가벼운 사람과 같이 탈 수 있는지 확인
# 4. 같이 탈 수 있으면 둘을 보내고, 못 타면 무거운 사람만 보낸다 -> 어느 쪽이든 배 한 척을 썼으니 answer +1