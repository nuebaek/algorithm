def solution(s):
    answer = ''
    words = s.split(" ", -1)
    for i in words:
        for j in range(len(i)):
            if j%2==0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        if i == " ":
             pass
        else:
            answer += " "
    answer = answer[:len(s)]
    return answer