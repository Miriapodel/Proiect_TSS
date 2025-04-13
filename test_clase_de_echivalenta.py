import pytest
from main import Solution


@pytest.fixture
def solution():
    return Solution()


def test_valid_sudoku(solution):
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
    assert solution.isValidSudoku(board)


def test_invalid_row_sudoku(solution):
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "5"],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert not solution.isValidSudoku(board)


def test_invalid_column_sudoku(solution):
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["5", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert not solution.isValidSudoku(board)


def test_invalid_subbox_sudoku(solution):
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", "5", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert not solution.isValidSudoku(board)


def test_board_with_wrong_number_of_rows(solution):
    board = [["."] * 9 for _ in range(8)]
    assert not solution.isValidSudoku(board)


def test_row_with_wrong_number_of_columns(solution):
    board = [["."] * 9 for _ in range(9)]
    board[3] = ["."] * 8
    assert not solution.isValidSudoku(board)


def test_board_with_invalid_characters(solution):
    board = [["."] * 9 for _ in range(9)]
    board[5][5] = "X"
    assert not solution.isValidSudoku(board)


def test_board_not_a_list_of_lists(solution):
    board = "abobonanaguagua"
    assert not solution.isValidSudoku(board)