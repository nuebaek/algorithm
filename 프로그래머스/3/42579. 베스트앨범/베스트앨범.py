def solution(genres, plays):
    answer = []
    total={}
    dic={}   
    
    for i, p in enumerate(plays):
        if genres[i] not in dic:
            dic[genres[i]]=[]
        dic[genres[i]].append([i, p])
        if genres[i] not in total:
            total[genres[i]]=0
        total[genres[i]]+=p
        
    genre_order = sorted(total, key=lambda g: total[g], reverse=True)

    for g in genre_order:
        sorted_songs = sorted(dic[g], key=lambda x: (-x[1], x[0]))
        answer.extend([idx for idx, _ in sorted_songs[:2]])
    return answer