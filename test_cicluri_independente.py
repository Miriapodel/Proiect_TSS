# test_solution_cycles.py
import pytest
from main import Solution

@pytest.fixture
def solution():
    return Solution()

# 1. valid_board_structure 1st if FALSE(isinstance)
def test_not_a_list(solution):
    board = "not_a_list"
    assert solution.isValidSudoku(board) == False

# 2. valid_board_structure 1st if FALSE(len)
def test_list_len_not_9(solution):
    board = [["."] * 9] * 8  # only 8 rows
    assert solution.isValidSudoku(board) == False

# 3. valid_board_structure 2nd if FALSE(isinstance)
def test_row_not_list(solution):
    board = ["row"] * 9  # rows are strings, not lists
    assert solution.isValidSudoku(board) == False

# 4. valid_board_structure 2nd if FALSE(len)
def test_row_len_not_9(solution):
    board = [["."] * 8] * 9  # only 8 columns per row
    assert solution.isValidSudoku(board) == False

# 5. valid_board_structure 3rd if FALSE(cell invalid)
def test_invalid_cell_value(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = "X"
    assert solution.isValidSudoku(board) == False

# 6.  valid_board_structure -> checkRowsAndColsForUniqueElems continue FALSE(board in rows)
def test_duplicate_in_row_with_continue(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = board[0][1] = "5"
    assert solution.isValidSudoku(board) == False

# 7. valid_board_structure -> checkRowsAndColsForUniqueElems continue FALSE(board in columns)
def test_duplicate_in_column_with_continue(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = board[1][0] = "8"
    assert solution.isValidSudoku(board) == False

# 8. valid_board_structure -> checkRowsAndColsForUniqueElems NO continue FALSE(board in rows)
def test_duplicate_in_row_no_continue(solution):
    board = [["1"] * 9 for _ in range(9)]
    assert solution.isValidSudoku(board) == False

# 9. valid_board_structure -> checkRowsAndColsForUniqueElems NO continue FALSE(board in colums)
def test_duplicate_in_column_no_continue(solution):
    board = [["."] * 9 for _ in range(9)]
    for i in range(9):
        board[i][0] = "9"
    assert solution.isValidSudoku(board) == False

# 10. valid_board_structure -> checkRowsAndColsForUniqueElems continue -> checkSubBox continue FALSE(board in elems)
def test_duplicate_in_subbox_continue(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = board[1][1] = "3"
    assert solution.isValidSudoku(board) == False

# 11. valid_board_structure -> checkRowsAndColsForUniqueElems continue -> checkSubBox NO continue FALSE(board in elems)
def test_duplicate_in_subbox_no_continue(solution):
    board = [["1"] * 9 for _ in range(9)]
    board[0][0] = board[0][1] = "7"
    assert solution.isValidSudoku(board) == False

# 12. valid_board_structure -> checkRowsAndColsForUniqueElems NO continue -> checkSubBox  continue FALSE(board in elems)
def test_no_continue_subbox_continue_false(solution):
    board = [["1"] * 9 for _ in range(9)]
    board[0][0] = "4"
    board[1][1] = "4"  # duplicat în subbox (0,0)
    assert solution.isValidSudoku(board) == False

# 13. valid_board_structure -> checkRowsAndColsForUniqueElems NO continue -> checkSubBox NO continue FALSE(board in elems)
def test_no_continue_subbox_no_continue_false(solution):
    board = [["9"] * 9 for _ in range(9)]
    board[3][3] = board[4][4] = "2"  # duplicat în subbox (4,4), fără puncte
    assert solution.isValidSudoku(board) == False

# 14. valid_board_structure -> checkRowsAndColsForUniqueElems continue -> checkSubBox continue TRUE
def test_valid_with_dots_and_subbox_continue(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = "5"
    board[1][1] = "6"
    board[2][2] = "7"
    assert solution.isValidSudoku(board) == True

# 15. valid_board_structure -> checkRowsAndColsForUniqueElems continue -> checkSubBox NO continue TRUE
def test_valid_no_dots_subbox(solution):
    board = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
    ]
    assert solution.isValidSudoku(board) == True

# 16. valid_board_structure -> checkRowsAndColsForUniqueElems NO continue -> checkSubBox continue TRUE
def test_valid_dense_board_continue_true(solution):
    board = [["9"] * 9 for _ in range(9)]
    for i in range(9):
        board[i][i] = "."
    assert solution.isValidSudoku(board) == False  # conflict remains

# 17. valid_board_structure -> checkRowsAndColsForUniqueElems NO continue -> checkSubBox NO continue TRUE
def test_fully_valid_custom(solution):
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert solution.isValidSudoku(board) == True