# Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. 
# The objective is to fill the grid with the constraint that every row, column, 
# and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

# Implement an efficient sudoku solver.

def find_next_empty(puzzle):
    for i in range(9):
        for j in range(9):
            if not puzzle[i][j]:
                return i, j
    
    return None, None


def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
        
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    return True
        


def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)
    
    if row is None:
        return True
        
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            
            if solve_sudoku(puzzle):
                return True
                
        puzzle[row][col] = 0
        
    return False
    
    
sample_board = [
    [3, 9, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 5],
    [0, 0, 0, 7, 1, 9, 0, 8, 0],
    [0, 5, 0, 0, 6, 8, 0, 0, 0],
    [2, 0, 6, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 4],
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 7, 0, 1, 0, 5, 0, 4, 0],
    [1, 0, 9, 0, 0, 0, 2, 0, 0]
]

print(solve_sudoku(sample_board))
print(sample_board)



'''
def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if not puzzle[r][c]:
                return r, c
    return None, None


def is_valid(r, c, val, puzzle):
    row_vals = puzzle[r]
    if val in row_vals:
        return False
    
    col_vals = [puzzle[r][i] for i in range(9)]
    if val in col_vals:
        return False
        
    row_start = (r // 3) * 3
    col_start = (c // 3) * 3
    
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if puzzle[i][j] == val:
                return False
    return True

    
def solve(sudoku):
    row, col = find_next_empty(sudoku)
    if row is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(row, col, guess, sudoku):
            sudoku[row][col] = guess
            if solve(sudoku):
                return True
            sudoku[row][col] = 0
    
    return False
'''