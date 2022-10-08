def find_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return r,c
    return None,None

def is_valid(puzzle,guess,row, col):
    rowvals=puzzle[row]
    if guess in rowvals:
        return False
    colvals=[]
    for i in range (9):
        colvals.append(puzzle[i][col])
    if guess in colvals:
        return False

    row_start=row//3 *3
    col_start=col//3 *3
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c]==guess:
                return False
    return True



def sudoku_solver(puzzle):

    row,col= find_empty(puzzle)

    if row==None:
        return True

    for guess in range(1,10):
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col]=guess

            if sudoku_solver(puzzle):
                return True

        puzzle[row][col]=-1

    return False

puzzle = [[9, -1, 6, -1, 4, 5, -1, 8, 1],
        [-1, -1, -1, -1, 2, -1, 4, 3, -1],
        [4, -1, -1, 8, -1, 1, -1, 2, 6],
        [-1, 6, 8, 9, 1, -1, -1, -1, 7],
        [-1, -1, -1, -1, -1, 4, -1, 6, 3],
        [-1, -1, -1, 6, -1, 7, 1, 9, -1],
        [6, -1, -1, 4, 7, -1, 3, 1, 2],
        [2, 1, -1, 5, -1, -1, 6, -1, -1],
        [-1, -1, 4, 1, -1, 2, -1, -1, -1]]

sudoku_solver(puzzle)
if sudoku_solver(puzzle):
    print ('u won')
    for x in puzzle:
        print (x)
else:
    'cant solve'