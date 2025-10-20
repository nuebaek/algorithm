answer = 0

def dfs(numbers, idx, result, target):
    global answer
    
    if len(numbers) == idx:
        if target == result:
            answer += 1
        return
    else:
        dfs(numbers, idx + 1, result + numbers[idx], target)
        dfs(numbers, idx + 1, result - numbers[idx], target)

def solution(numbers, target):
    global answer
    answer = 0 
    dfs(numbers, 0, 0, target)
    return answer