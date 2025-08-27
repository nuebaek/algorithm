def solution(quiz):
    answer = []
    for i in quiz:
        count = i.split(" ")
        if count[1] == "+":
            if int(count[0]) + int(count[2]) == int(count[4]):
                answer.append("O")
            else:
                answer.append("X")
        elif count[1] == "-":
            if int(count[0]) - int(count[2]) == int(count[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer