import pytest
from main import Solution


@pytest.fixture
def solution():
    return Solution()


def test_valid_board_structure_all_valid(solution):
    board = [["."] * 9 for _ in range(9)]
    assert solution.valid_board_structure(board) == True


def test_invalid_not_list(solution):
    board = "not a list"
    assert solution.valid_board_structure(board) == False


def test_invalid_row_count(solution):
    board = [["."] * 9 for _ in range(8)]
    assert solution.valid_board_structure(board) == False


def test_invalid_row_type(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0] = "123456789"
    assert solution.valid_board_structure(board) == False


def test_invalid_column_count(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0] = ["."] * 8
    assert solution.valid_board_structure(board) == False


def test_invalid_cell_value(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = "X"
    assert solution.valid_board_structure(board) == False


def test_fully_valid_sudoku(solution):
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
    assert solution.isValidSudoku(board)


def test_duplicate_in_row(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = "1"
    board[0][1] = "1"
    assert not solution.isValidSudoku(board)


def test_duplicate_in_column(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = "1"
    board[1][0] = "1"
    assert not solution.isValidSudoku(board)


def test_duplicate_in_subbox(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = "1"
    board[1][1] = "1"
    assert not solution.isValidSudoku(board)


def test_invalid_structure_fails_sudoku(solution):
    board = [["."] * 9 for _ in range(8)]
    assert not solution.isValidSudoku(board)
