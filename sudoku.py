def sudoku(board):
    if(checkrows(board) and check_columns(board) and check_3x3(board)