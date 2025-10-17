def solution(brown, yellow):
    num = brown + yellow
    num_list = []
    for i in range(1, (num//2)+1):
        if num % i == 0:
            k = num//i
            num_list.append([i, k])
    
    num_list.sort(key=lambda x:-x[0])
    
    for [x, y] in num_list:
        if (2*x)+2*(y-2)==brown and x>=y:
            return [x, y]