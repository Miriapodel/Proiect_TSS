def valid_board_structure(self, board):
    valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    if not isinstance(board, list) or len(board) != 9:
        return False

    for row in board:
        if not isinstance(row, list) or len(row) != 9:
            return False

        for cell in row:
            if cell not in valid_characters:
                return False

    return True


def isValidSudoku(self, board):
    if not self.valid_board_structure(board):
        return False
    else:
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