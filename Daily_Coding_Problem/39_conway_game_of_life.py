# Conway's Game of Life takes place on an infinite two-dimensional board of square cells. 
# Each cell is either dead or alive, and at each tick, the following rules apply:

# Any live cell with less than two live neighbours dies.
# Any live cell with two or three live neighbours remains living.
# Any live cell with more than three live neighbours dies.
# Any dead cell with exactly three live neighbours becomes a live cell.
# A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

# Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates 
# and the number of steps it should run for. Once initialized, it should print out the board state at each step. 
# Since it's an infinite board, print out only the relevant coordinates, 
# i.e. from the top-leftmost live cell to bottom-rightmost live cell.

# You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).



grid = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '*', '*', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '*', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '*', '*', '.', '.', '.', '.', '.'],
        ['.', '.', '*', '*', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '*', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '*', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
       ]
size = 10

rows = [-1, 0, 1, -1, 1, -1, 0, 1]
cols = [-1, -1, -1, 0, 0, 1, 1, 1]


def count_live_neighbours(r, c):
    count = 0
    for i in range(8):
        p = r + rows[i]
        q = c + cols[i]
        if (0 <= p < 10) and (0 <= q < 10) and grid[p][q] == '*':
            count += 1
    return count


def apply_rules():
    for i in range(size):
        for j in range(size):
            c = count_live_neighbours(i, j)
            if grid[i][j] == '*':
                if c < 2 or c > 3:
                    grid[i][j] = '.'
            else:
                if c == 3:
                    grid[i][j] = '*'


def printIteration():
    for row in grid:
        print(*row)


def start_game(n):
    for i in range(n):
        apply_rules()
        print(f'Iteration {i + 1} :')
        printIteration()


iterations = int(input('Enter no.of iterations :'))
start_game(iterations)