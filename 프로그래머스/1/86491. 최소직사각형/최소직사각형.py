def solution(sizes):
    h, w = 0, 0
    
    for s in sizes:
        if s[0] < s[1]:
            s[0], s[1] = s[1], s[0]
        if h < s[0]:
            h = s[0]
        if w < s[1]:
            w = s[1]
            
    return h*w
