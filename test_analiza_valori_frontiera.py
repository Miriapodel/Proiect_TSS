import pytest
from main import Solution

@pytest.fixture
def solution():
    return Solution()

# Dimensiuni corecte
def test_valid_board_structure(solution):
    board = [["."] * 9 for _ in range(9)]
    assert solution.valid_board_structure(board) == True

# Dimensiune invalida (8 randuri)
def test_too_few_rows(solution):
    board = [["."] * 9 for _ in range(8)]
    assert solution.valid_board_structure(board) == False

#  Dimensiune invalida (10 randuri)
def test_too_many_rows(solution):
    board = [["."] * 9 for _ in range(10)]
    assert solution.valid_board_structure(board) == False

#  Dimensiune invalida (un rand are 8 coloane)
def test_row_with_too_few_columns(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0] = ["."] * 8
    assert solution.valid_board_structure(board) == False

#  Dimensiune invalida (un rand are 10 coloane)
def test_row_with_too_many_columns(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0] = ["."] * 10
    assert solution.valid_board_structure(board) == False

#  Valoare invalida - 0
def test_invalid_cell_value_zero(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = "0"
    assert solution.valid_board_structure(board) == False

#  Valoare invalida - 10
def test_invalid_cell_value_ten(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0][1] = "10"
    assert solution.valid_board_structure(board) == False

#  Valoare invalida - #
def test_invalid_cell_value_symbol(solution):
    board = [["."] * 9 for _ in range(9)]
    board[1][1] = "#"
    assert solution.valid_board_structure(board) == False

#  Valori la margini corecte - 1 si 9
def test_valid_cell_values_at_boundaries(solution):
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = "1"
    board[8][8] = "9"
    assert solution.valid_board_structure(board) == True