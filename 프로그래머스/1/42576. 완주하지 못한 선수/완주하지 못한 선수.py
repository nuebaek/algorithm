def solution(participant, completion):
    hashdict={}
    hashcount=0
    
    for i in participant:
        hashdict[hash(i)]=i
        hashcount += hash(i)
    
    for j in completion:
        hashcount -= hash(j)
    
    return hashdict[hashcount] 