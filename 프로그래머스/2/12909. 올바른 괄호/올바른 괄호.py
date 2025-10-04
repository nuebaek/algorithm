def solution(s):
    total = []
    for i in s:
        if i=="(":
            total.append(i)
        elif len(total)>0 and i==")":
            total.pop()
        elif len(total)==0 and i==")":
            return False
    if len(total)==0:
        return True
    else:
        return False
    return True

