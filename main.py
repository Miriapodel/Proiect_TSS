from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)

        def checkRowsAndColsForUniqueElems():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        continue

                    if board[i][j] in rows[i] or board[i][j] in columns[j]:
                        return False

                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])

            return True

        def checkSubBox(noOfBox):
            elems = set()
            startingRow = (noOfBox // 3) * 3
            startingColumn = (noOfBox % 3) * 3

            for i in range(startingRow, startingRow + 3):
                for j in range(startingColumn, startingColumn + 3):
                    if board[i][j] == ".":
                        continue

                    if board[i][j] in elems:
                        return False

                    elems.add(board[i][j])

            return True

        if not checkRowsAndColsForUniqueElems():
            return False

        for i in range(9):
            if not checkSubBox(i):
                return False

        return True


import pytest


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
