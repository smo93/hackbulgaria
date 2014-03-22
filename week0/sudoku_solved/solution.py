# chechs if the row/col/block is valid
def is_valid(lst):
    return sorted(lst) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sudoku_solved(sudoku):
    for i in range(9):
        row = sudoku[i]
        col = [r[i] for r in sudoku]

        if not is_valid(row) and not is_valid(col):
            return False

    for i in range(3):
        for j in range(3):
            block = [sudoku[x][y] for x in range(0 + i * 3, 3 + i * 3)
                    for y in range(0 + j * 3, 3 + j * 3)]
            if not is_valid(block):
                return False

    return True
