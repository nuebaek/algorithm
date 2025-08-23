def solution(score):
    # 평균 점수 구하기
    avg_scores = [sum(s) / len(s) for s in score]
    # 내림차순 정렬
    sorted_scores = sorted(avg_scores, reverse=True)
    # 등수 매기기
    ranks = [sorted_scores.index(avg) + 1 for avg in avg_scores]
    return ranks