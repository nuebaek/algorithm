def solution(nums):
    dic = {}
    answer = 0
    for i in nums:
        dic[i] = dic.get(i, 0)+1
    if len(dic) > len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(dic)
    return answer
