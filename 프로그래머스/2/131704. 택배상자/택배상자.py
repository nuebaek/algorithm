def solution(order):
    sub = []          
    next_box = 1     
    answer = 0

    for target in order:
        if sub and sub[-1] == target:
            sub.pop()

        else:
            while next_box < target:
                sub.append(next_box)
                next_box += 1

            if next_box != target:
                break

            next_box += 1

        answer += 1

    return answer


# 1. 상자는 컨테이너 벨트에서 1, 2, 3, ... 순서로 나온다.
# 2. order를 앞에서부터 보며, 지금 트럭에 실어야 할 상자를 확인한다.
# 3. 그 상자가 보조 스택 맨 위에 있으면, 스택에서 꺼내 트럭에 싣는다.
# 4. 스택 맨 위에 없으면 컨테이너 벨트에서 상자가 나오는 순서대로 확인한다.
# 5. 목표 상자보다 앞에 나온 상자는 보조 스택에 넣고, 목표 상자는 트럭에 싣는다.
# 6. 목표 상자를 스택에서도 컨테이너 벨트에서도 꺼낼 수 없으면 더 실을 수 없으니 멈춘다.
# 7. 트럭에 실은 상자 수를 반환한다.
