import sys

input = sys.stdin.readline
sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

row_chk = [[False] * 10 for _ in range(9)]
col_chk = [[False] * 10 for _ in range(9)]
sq_chk = [[False] * 10 for _ in range(9)]

for r in range(9):
    for c in range(9):
        if sudoku[r][c] != 0:
            num = sudoku[r][c]
            row_chk[r][num] = True
            col_chk[c][num] = True
            sq_chk[(r // 3) * 3 + (c // 3)][num] = True

def solve(idx):
    if idx == len(zeros):
        for row in sudoku:
            print(*row)
        exit()
    
    r, c = zeros[idx]
    sq_idx = (r // 3) * 3 + (c // 3) 
    
    for n in range(1, 10):
        if not row_chk[r][n] and not col_chk[c][n] and not sq_chk[sq_idx][n]:
            sudoku[r][c] = n
            row_chk[r][n] = col_chk[c][n] = sq_chk[sq_idx][n] = True
            solve(idx + 1)
            sudoku[r][c] = 0
            row_chk[r][n] = col_chk[c][n] = sq_chk[sq_idx][n] = False

solve(0)