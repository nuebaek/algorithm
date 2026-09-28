def solution(places):
    answer = []
    
    def check(x):
        """사람 좌표 구하기"""
        people = []
        
        for i in range(5):
            for j in range(5):
                if x[i][j] == "P":
                    people.append((i, j))

        for k in range(len(people)):
            for l in range(k + 1, len(people)):
                i, j = people[k]
                a, b = people[l]
                distance = abs(i-a) + abs(j-b)

                if distance == 1:
                    return 0

                if distance == 2:
                    if i == a and x[i][(j+b)//2] != "X":
                        return 0
                    if j == b and x[(i+a)//2][j] != "X":
                        return 0
                    if i != a and j != b:
                        if x[i][b] != "X" or x[a][j] != "X":
                            return 0
        
        return 1
        
        
    for p in places:
        ans = check(p)
        answer.append(ans)

    return answer



# 1. 대기실은 5개, 각각 5*5
# 2. 사람 두 명씩 골라 맨해튼 거리 구하기
# 3. 거리가 1이면 바로 0
# 4. 거리가 2이면 사이에 파티션이 있는지 확인
# 5. 규칙을 지켰으면 1