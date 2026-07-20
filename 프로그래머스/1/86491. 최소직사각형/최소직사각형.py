def solution(sizes):
    rows, cols = [], []
    
    for s in sizes:
        rows.append(max(s))
        cols.append(min(s))
        
    return max(rows)*max(cols)
