def solution(answers):
    user1 = [1, 2, 3, 4, 5]
    user2 = [2, 1, 2, 3, 2, 4, 2, 5]
    user3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    users = [user1, user2, user3]
    
    results = []
    max_num = 0
    
    for i in range(3):
        q = len(answers) // len(users[i])
        r = len(answers) % len(users[i])
        if q == 0:
            users[i] = users[i][:r]
            
        users[i] = users[i] * q + users[i][:r]
        result = [a - b for a, b in zip(users[i], answers)]
        
        if max_num <= result.count(0):
            if max_num == result.count(0):
                results.append(i+1)
            else:
                max_num = result.count(0)
                results = [i+1]
            
    return results
    