def solution(polynomial):
    count = polynomial.split(" + ")
    x = 0
    num = 0
    for i in count:
        if i.endswith("x"):
            if i == "x":
                x += 1
            else:
                x += int(i[:-1])
        else:
            num += int(i)
            
    if x == 0:
        return str(num)
    elif num == 0:
        return "x" if x == 1 else str(x) + "x"
    else:
        return ("x" if x == 1 else str(x) + "x") + " + " + str(num)