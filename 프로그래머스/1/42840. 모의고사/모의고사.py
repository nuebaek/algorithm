def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    patterns = [p1, p2, p3]

    scores = [0, 0, 0]
    for i, ans in enumerate(answers):
        for idx, pattern in enumerate(patterns):
            if ans == pattern[i % len(pattern)]:
                scores[idx] += 1

    best = max(scores)
    return [i + 1 for i, s in enumerate(scores) if s == best]