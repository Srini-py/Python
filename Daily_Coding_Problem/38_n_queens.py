# You have an N by N board. Write a function that, given N, 
# returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, 
# i.e. no two queens share the same row, column, or diagonal.


def isValid(board, r, c, n):

    #rows check
    rows = board[r]
    if any(rows):
        return False
    
    #cols check
    cols = [board[i][c] for i in range(n)]
    if any(cols):
        return False
        
    #diagonal1 check
    if r > c:
        diff = r - c
        diag1 = [board[i + diff][i] for i in range(n - diff)]
    else:
        diff = c - r
        diag1 = [board[i][i + diff] for i in range(n - diff)]
    if any(diag1):
        return False
    
    #diagonal2 check
    x_diff = n - 1 - r
    y_diff = c
    if x_diff >= y_diff:
        diag2 = [board[r + c - i][i] for i in range(r + c + 1)]
    else:
        diag2 = [board[n - i - 1][y_diff - x_diff + i] for i in range(n - y_diff + x_diff)]
    if any(diag2):
        return False
    
    return True
    


def place_n_queens(board, n, queens_placed):
    if queens_placed >= n:
        return True
    for i in range(n):
        if isValid(board, i, queens_placed, n):
            board[i][queens_placed] = 1
            if place_n_queens(board, n, queens_placed + 1):
                return True
        board[i][queens_placed] = 0
    return False


n = int(input('Enter the size of the board :'))
board = [[0 for i in range(n)] for j in range(n)]
place_n_queens(board, n, 0)
print(board)