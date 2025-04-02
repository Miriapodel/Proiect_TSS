
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


from typing import List
from collections import defaultdict


class Solution:
    def xǁSolutionǁvalid_board_structure__mutmut_orig(self, board):
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
    def xǁSolutionǁvalid_board_structure__mutmut_1(self, board):
        valid_characters = {"XX.XX", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_2(self, board):
        valid_characters = {".", "XX1XX", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_3(self, board):
        valid_characters = {".", "1", "XX2XX", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_4(self, board):
        valid_characters = {".", "1", "2", "XX3XX", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_5(self, board):
        valid_characters = {".", "1", "2", "3", "XX4XX", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_6(self, board):
        valid_characters = {".", "1", "2", "3", "4", "XX5XX", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_7(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "XX6XX", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_8(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "XX7XX", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_9(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "XX8XX", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_10(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "XX9XX"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_11(self, board):
        valid_characters = None

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_12(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if  isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_13(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) == 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_14(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 10:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_15(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) and len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_16(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return True

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_17(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if  isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_18(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) == 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_19(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 10:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_20(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) and len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_21(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return True

            for cell in row:
                if cell not in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_22(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell  in valid_characters:
                    return False

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_23(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return True

        return True
    def xǁSolutionǁvalid_board_structure__mutmut_24(self, board):
        valid_characters = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if not isinstance(board, list) or len(board) != 9:
            return False

        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False

            for cell in row:
                if cell not in valid_characters:
                    return False

        return False

    xǁSolutionǁvalid_board_structure__mutmut_mutants = {
    'xǁSolutionǁvalid_board_structure__mutmut_1': xǁSolutionǁvalid_board_structure__mutmut_1, 
        'xǁSolutionǁvalid_board_structure__mutmut_2': xǁSolutionǁvalid_board_structure__mutmut_2, 
        'xǁSolutionǁvalid_board_structure__mutmut_3': xǁSolutionǁvalid_board_structure__mutmut_3, 
        'xǁSolutionǁvalid_board_structure__mutmut_4': xǁSolutionǁvalid_board_structure__mutmut_4, 
        'xǁSolutionǁvalid_board_structure__mutmut_5': xǁSolutionǁvalid_board_structure__mutmut_5, 
        'xǁSolutionǁvalid_board_structure__mutmut_6': xǁSolutionǁvalid_board_structure__mutmut_6, 
        'xǁSolutionǁvalid_board_structure__mutmut_7': xǁSolutionǁvalid_board_structure__mutmut_7, 
        'xǁSolutionǁvalid_board_structure__mutmut_8': xǁSolutionǁvalid_board_structure__mutmut_8, 
        'xǁSolutionǁvalid_board_structure__mutmut_9': xǁSolutionǁvalid_board_structure__mutmut_9, 
        'xǁSolutionǁvalid_board_structure__mutmut_10': xǁSolutionǁvalid_board_structure__mutmut_10, 
        'xǁSolutionǁvalid_board_structure__mutmut_11': xǁSolutionǁvalid_board_structure__mutmut_11, 
        'xǁSolutionǁvalid_board_structure__mutmut_12': xǁSolutionǁvalid_board_structure__mutmut_12, 
        'xǁSolutionǁvalid_board_structure__mutmut_13': xǁSolutionǁvalid_board_structure__mutmut_13, 
        'xǁSolutionǁvalid_board_structure__mutmut_14': xǁSolutionǁvalid_board_structure__mutmut_14, 
        'xǁSolutionǁvalid_board_structure__mutmut_15': xǁSolutionǁvalid_board_structure__mutmut_15, 
        'xǁSolutionǁvalid_board_structure__mutmut_16': xǁSolutionǁvalid_board_structure__mutmut_16, 
        'xǁSolutionǁvalid_board_structure__mutmut_17': xǁSolutionǁvalid_board_structure__mutmut_17, 
        'xǁSolutionǁvalid_board_structure__mutmut_18': xǁSolutionǁvalid_board_structure__mutmut_18, 
        'xǁSolutionǁvalid_board_structure__mutmut_19': xǁSolutionǁvalid_board_structure__mutmut_19, 
        'xǁSolutionǁvalid_board_structure__mutmut_20': xǁSolutionǁvalid_board_structure__mutmut_20, 
        'xǁSolutionǁvalid_board_structure__mutmut_21': xǁSolutionǁvalid_board_structure__mutmut_21, 
        'xǁSolutionǁvalid_board_structure__mutmut_22': xǁSolutionǁvalid_board_structure__mutmut_22, 
        'xǁSolutionǁvalid_board_structure__mutmut_23': xǁSolutionǁvalid_board_structure__mutmut_23, 
        'xǁSolutionǁvalid_board_structure__mutmut_24': xǁSolutionǁvalid_board_structure__mutmut_24
    }

    def valid_board_structure(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSolutionǁvalid_board_structure__mutmut_orig"), object.__getattribute__(self, "xǁSolutionǁvalid_board_structure__mutmut_mutants"), *args, **kwargs)
        return result 

    valid_board_structure.__signature__ = _mutmut_signature(xǁSolutionǁvalid_board_structure__mutmut_orig)
    xǁSolutionǁvalid_board_structure__mutmut_orig.__name__ = 'xǁSolutionǁvalid_board_structure'




    def xǁSolutionǁisValidSudoku__mutmut_orig(self, board):

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


    def xǁSolutionǁisValidSudoku__mutmut_1(self, board):

        if  self.valid_board_structure(board):
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


    def xǁSolutionǁisValidSudoku__mutmut_2(self, board):

        if not self.valid_board_structure(None):
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


    def xǁSolutionǁisValidSudoku__mutmut_3(self, board):

        if not self.valid_board_structure(board):
            return True
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


    def xǁSolutionǁisValidSudoku__mutmut_4(self, board):

        if not self.valid_board_structure(board):
            return False
        else:
            columns = defaultdict(None)
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


    def xǁSolutionǁisValidSudoku__mutmut_5(self, board):

        if not self.valid_board_structure(board):
            return False
        else:
            columns = None
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


    def xǁSolutionǁisValidSudoku__mutmut_6(self, board):

        if not self.valid_board_structure(board):
            return False
        else:
            columns = defaultdict(set)
            rows = defaultdict(None)

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


    def xǁSolutionǁisValidSudoku__mutmut_7(self, board):

        if not self.valid_board_structure(board):
            return False
        else:
            columns = defaultdict(set)
            rows = None

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


    def xǁSolutionǁisValidSudoku__mutmut_8(self, board):

        if not self.valid_board_structure(board):
            return False
        else:
            columns = defaultdict(set)
            rows = defaultdict(set)

            def checkRowsAndColsForUniqueElems():
                for i in range(10):
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


    def xǁSolutionǁisValidSudoku__mutmut_9(self, board):

        if not self.valid_board_structure(board):
            return False
        else:
            columns = defaultdict(set)
            rows = defaultdict(set)

            def checkRowsAndColsForUniqueElems():
                for i in range(9):
                    for j in range(10):
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


    def xǁSolutionǁisValidSudoku__mutmut_10(self, board):

        if not self.valid_board_structure(board):
            return False
        else:
            columns = defaultdict(set)
            rows = defaultdict(set)

            def checkRowsAndColsForUniqueElems():
                for i in range(9):
                    for j in range(9):
                        if board[None][j] == ".":
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


    def xǁSolutionǁisValidSudoku__mutmut_11(self, board):

        if not self.valid_board_structure(board):
            return False
        else:
            columns = defaultdict(set)
            rows = defaultdict(set)

            def checkRowsAndColsForUniqueElems():
                for i in range(9):
                    for j in range(9):
                        if board[i][None] == ".":
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


    def xǁSolutionǁisValidSudoku__mutmut_12(self, board):

        if not self.valid_board_structure(board):
            return False
        else:
            columns = defaultdict(set)
            rows = defaultdict(set)

            def checkRowsAndColsForUniqueElems():
                for i in range(9):
                    for j in range(9):
                        if board[i][j] != ".":
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


    def xǁSolutionǁisValidSudoku__mutmut_13(self, board):

        if not self.valid_board_structure(board):
            return False
        else:
            columns = defaultdict(set)
            rows = defaultdict(set)

            def checkRowsAndColsForUniqueElems():
                for i in range(9):
                    for j in range(9):
                        if board[i][j] == "XX.XX":
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


    def xǁSolutionǁisValidSudoku__mutmut_14(self, board):

        if not self.valid_board_structure(board):
            return False
        else:
            columns = defaultdict(set)
            rows = defaultdict(set)

            def checkRowsAndColsForUniqueElems():
                for i in range(9):
                    for j in range(9):
                        if board[i][j] == ".":
                            break

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


    def xǁSolutionǁisValidSudoku__mutmut_15(self, board):

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

                        if board[None][j] in rows[i] or board[i][j] in columns[j]:
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


    def xǁSolutionǁisValidSudoku__mutmut_16(self, board):

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

                        if board[i][None] in rows[i] or board[i][j] in columns[j]:
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


    def xǁSolutionǁisValidSudoku__mutmut_17(self, board):

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

                        if board[i][j] not in rows[i] or board[i][j] in columns[j]:
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


    def xǁSolutionǁisValidSudoku__mutmut_18(self, board):

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

                        if board[i][j] in rows[None] or board[i][j] in columns[j]:
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


    def xǁSolutionǁisValidSudoku__mutmut_19(self, board):

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

                        if board[i][j] in rows[i] or board[None][j] in columns[j]:
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


    def xǁSolutionǁisValidSudoku__mutmut_20(self, board):

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

                        if board[i][j] in rows[i] or board[i][None] in columns[j]:
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


    def xǁSolutionǁisValidSudoku__mutmut_21(self, board):

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

                        if board[i][j] in rows[i] or board[i][j] not in columns[j]:
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


    def xǁSolutionǁisValidSudoku__mutmut_22(self, board):

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

                        if board[i][j] in rows[i] or board[i][j] in columns[None]:
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


    def xǁSolutionǁisValidSudoku__mutmut_23(self, board):

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

                        if board[i][j] in rows[i] and board[i][j] in columns[j]:
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


    def xǁSolutionǁisValidSudoku__mutmut_24(self, board):

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
                            return True

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


    def xǁSolutionǁisValidSudoku__mutmut_25(self, board):

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

                        rows[None].add(board[i][j])
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


    def xǁSolutionǁisValidSudoku__mutmut_26(self, board):

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

                        rows[i].add(board[None][j])
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


    def xǁSolutionǁisValidSudoku__mutmut_27(self, board):

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

                        rows[i].add(board[i][None])
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


    def xǁSolutionǁisValidSudoku__mutmut_28(self, board):

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
                        columns[None].add(board[i][j])

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


    def xǁSolutionǁisValidSudoku__mutmut_29(self, board):

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
                        columns[j].add(board[None][j])

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


    def xǁSolutionǁisValidSudoku__mutmut_30(self, board):

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
                        columns[j].add(board[i][None])

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


    def xǁSolutionǁisValidSudoku__mutmut_31(self, board):

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

                return False

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


    def xǁSolutionǁisValidSudoku__mutmut_32(self, board):

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
                elems = None
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


    def xǁSolutionǁisValidSudoku__mutmut_33(self, board):

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
                startingRow = (noOfBox / 3) * 3
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


    def xǁSolutionǁisValidSudoku__mutmut_34(self, board):

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
                startingRow = (noOfBox // 4) * 3
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


    def xǁSolutionǁisValidSudoku__mutmut_35(self, board):

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
                startingRow = (noOfBox // 3) / 3
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


    def xǁSolutionǁisValidSudoku__mutmut_36(self, board):

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
                startingRow = (noOfBox // 3) * 4
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


    def xǁSolutionǁisValidSudoku__mutmut_37(self, board):

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
                startingRow = None
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


    def xǁSolutionǁisValidSudoku__mutmut_38(self, board):

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
                startingColumn = (noOfBox / 3) * 3

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


    def xǁSolutionǁisValidSudoku__mutmut_39(self, board):

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
                startingColumn = (noOfBox % 4) * 3

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


    def xǁSolutionǁisValidSudoku__mutmut_40(self, board):

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
                startingColumn = (noOfBox % 3) / 3

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


    def xǁSolutionǁisValidSudoku__mutmut_41(self, board):

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
                startingColumn = (noOfBox % 3) * 4

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


    def xǁSolutionǁisValidSudoku__mutmut_42(self, board):

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
                startingColumn = None

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


    def xǁSolutionǁisValidSudoku__mutmut_43(self, board):

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

                for i in range(None, startingRow + 3):
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


    def xǁSolutionǁisValidSudoku__mutmut_44(self, board):

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

                for i in range(startingRow, startingRow - 3):
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


    def xǁSolutionǁisValidSudoku__mutmut_45(self, board):

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

                for i in range(startingRow, startingRow + 4):
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


    def xǁSolutionǁisValidSudoku__mutmut_46(self, board):

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

                for i in range( startingRow + 3):
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


    def xǁSolutionǁisValidSudoku__mutmut_47(self, board):

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
                    for j in range(None, startingColumn + 3):
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


    def xǁSolutionǁisValidSudoku__mutmut_48(self, board):

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
                    for j in range(startingColumn, startingColumn - 3):
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


    def xǁSolutionǁisValidSudoku__mutmut_49(self, board):

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
                    for j in range(startingColumn, startingColumn + 4):
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


    def xǁSolutionǁisValidSudoku__mutmut_50(self, board):

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
                    for j in range( startingColumn + 3):
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


    def xǁSolutionǁisValidSudoku__mutmut_51(self, board):

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
                        if board[None][j] == ".":
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


    def xǁSolutionǁisValidSudoku__mutmut_52(self, board):

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
                        if board[i][None] == ".":
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


    def xǁSolutionǁisValidSudoku__mutmut_53(self, board):

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
                        if board[i][j] != ".":
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


    def xǁSolutionǁisValidSudoku__mutmut_54(self, board):

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
                        if board[i][j] == "XX.XX":
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


    def xǁSolutionǁisValidSudoku__mutmut_55(self, board):

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
                            break

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


    def xǁSolutionǁisValidSudoku__mutmut_56(self, board):

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

                        if board[None][j] in elems:
                            return False

                        elems.add(board[i][j])

                return True

            if not checkRowsAndColsForUniqueElems():
                return False

            for i in range(9):
                if not checkSubBox(i):
                    return False

            return True


    def xǁSolutionǁisValidSudoku__mutmut_57(self, board):

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

                        if board[i][None] in elems:
                            return False

                        elems.add(board[i][j])

                return True

            if not checkRowsAndColsForUniqueElems():
                return False

            for i in range(9):
                if not checkSubBox(i):
                    return False

            return True


    def xǁSolutionǁisValidSudoku__mutmut_58(self, board):

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

                        if board[i][j] not in elems:
                            return False

                        elems.add(board[i][j])

                return True

            if not checkRowsAndColsForUniqueElems():
                return False

            for i in range(9):
                if not checkSubBox(i):
                    return False

            return True


    def xǁSolutionǁisValidSudoku__mutmut_59(self, board):

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
                            return True

                        elems.add(board[i][j])

                return True

            if not checkRowsAndColsForUniqueElems():
                return False

            for i in range(9):
                if not checkSubBox(i):
                    return False

            return True


    def xǁSolutionǁisValidSudoku__mutmut_60(self, board):

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

                        elems.add(board[None][j])

                return True

            if not checkRowsAndColsForUniqueElems():
                return False

            for i in range(9):
                if not checkSubBox(i):
                    return False

            return True


    def xǁSolutionǁisValidSudoku__mutmut_61(self, board):

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

                        elems.add(board[i][None])

                return True

            if not checkRowsAndColsForUniqueElems():
                return False

            for i in range(9):
                if not checkSubBox(i):
                    return False

            return True


    def xǁSolutionǁisValidSudoku__mutmut_62(self, board):

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

                return False

            if not checkRowsAndColsForUniqueElems():
                return False

            for i in range(9):
                if not checkSubBox(i):
                    return False

            return True


    def xǁSolutionǁisValidSudoku__mutmut_63(self, board):

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

            if  checkRowsAndColsForUniqueElems():
                return False

            for i in range(9):
                if not checkSubBox(i):
                    return False

            return True


    def xǁSolutionǁisValidSudoku__mutmut_64(self, board):

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
                return True

            for i in range(9):
                if not checkSubBox(i):
                    return False

            return True


    def xǁSolutionǁisValidSudoku__mutmut_65(self, board):

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

            for i in range(10):
                if not checkSubBox(i):
                    return False

            return True


    def xǁSolutionǁisValidSudoku__mutmut_66(self, board):

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
                if  checkSubBox(i):
                    return False

            return True


    def xǁSolutionǁisValidSudoku__mutmut_67(self, board):

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
                if not checkSubBox(None):
                    return False

            return True


    def xǁSolutionǁisValidSudoku__mutmut_68(self, board):

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
                    return True

            return True


    def xǁSolutionǁisValidSudoku__mutmut_69(self, board):

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

            return False

    xǁSolutionǁisValidSudoku__mutmut_mutants = {
    'xǁSolutionǁisValidSudoku__mutmut_1': xǁSolutionǁisValidSudoku__mutmut_1, 
        'xǁSolutionǁisValidSudoku__mutmut_2': xǁSolutionǁisValidSudoku__mutmut_2, 
        'xǁSolutionǁisValidSudoku__mutmut_3': xǁSolutionǁisValidSudoku__mutmut_3, 
        'xǁSolutionǁisValidSudoku__mutmut_4': xǁSolutionǁisValidSudoku__mutmut_4, 
        'xǁSolutionǁisValidSudoku__mutmut_5': xǁSolutionǁisValidSudoku__mutmut_5, 
        'xǁSolutionǁisValidSudoku__mutmut_6': xǁSolutionǁisValidSudoku__mutmut_6, 
        'xǁSolutionǁisValidSudoku__mutmut_7': xǁSolutionǁisValidSudoku__mutmut_7, 
        'xǁSolutionǁisValidSudoku__mutmut_8': xǁSolutionǁisValidSudoku__mutmut_8, 
        'xǁSolutionǁisValidSudoku__mutmut_9': xǁSolutionǁisValidSudoku__mutmut_9, 
        'xǁSolutionǁisValidSudoku__mutmut_10': xǁSolutionǁisValidSudoku__mutmut_10, 
        'xǁSolutionǁisValidSudoku__mutmut_11': xǁSolutionǁisValidSudoku__mutmut_11, 
        'xǁSolutionǁisValidSudoku__mutmut_12': xǁSolutionǁisValidSudoku__mutmut_12, 
        'xǁSolutionǁisValidSudoku__mutmut_13': xǁSolutionǁisValidSudoku__mutmut_13, 
        'xǁSolutionǁisValidSudoku__mutmut_14': xǁSolutionǁisValidSudoku__mutmut_14, 
        'xǁSolutionǁisValidSudoku__mutmut_15': xǁSolutionǁisValidSudoku__mutmut_15, 
        'xǁSolutionǁisValidSudoku__mutmut_16': xǁSolutionǁisValidSudoku__mutmut_16, 
        'xǁSolutionǁisValidSudoku__mutmut_17': xǁSolutionǁisValidSudoku__mutmut_17, 
        'xǁSolutionǁisValidSudoku__mutmut_18': xǁSolutionǁisValidSudoku__mutmut_18, 
        'xǁSolutionǁisValidSudoku__mutmut_19': xǁSolutionǁisValidSudoku__mutmut_19, 
        'xǁSolutionǁisValidSudoku__mutmut_20': xǁSolutionǁisValidSudoku__mutmut_20, 
        'xǁSolutionǁisValidSudoku__mutmut_21': xǁSolutionǁisValidSudoku__mutmut_21, 
        'xǁSolutionǁisValidSudoku__mutmut_22': xǁSolutionǁisValidSudoku__mutmut_22, 
        'xǁSolutionǁisValidSudoku__mutmut_23': xǁSolutionǁisValidSudoku__mutmut_23, 
        'xǁSolutionǁisValidSudoku__mutmut_24': xǁSolutionǁisValidSudoku__mutmut_24, 
        'xǁSolutionǁisValidSudoku__mutmut_25': xǁSolutionǁisValidSudoku__mutmut_25, 
        'xǁSolutionǁisValidSudoku__mutmut_26': xǁSolutionǁisValidSudoku__mutmut_26, 
        'xǁSolutionǁisValidSudoku__mutmut_27': xǁSolutionǁisValidSudoku__mutmut_27, 
        'xǁSolutionǁisValidSudoku__mutmut_28': xǁSolutionǁisValidSudoku__mutmut_28, 
        'xǁSolutionǁisValidSudoku__mutmut_29': xǁSolutionǁisValidSudoku__mutmut_29, 
        'xǁSolutionǁisValidSudoku__mutmut_30': xǁSolutionǁisValidSudoku__mutmut_30, 
        'xǁSolutionǁisValidSudoku__mutmut_31': xǁSolutionǁisValidSudoku__mutmut_31, 
        'xǁSolutionǁisValidSudoku__mutmut_32': xǁSolutionǁisValidSudoku__mutmut_32, 
        'xǁSolutionǁisValidSudoku__mutmut_33': xǁSolutionǁisValidSudoku__mutmut_33, 
        'xǁSolutionǁisValidSudoku__mutmut_34': xǁSolutionǁisValidSudoku__mutmut_34, 
        'xǁSolutionǁisValidSudoku__mutmut_35': xǁSolutionǁisValidSudoku__mutmut_35, 
        'xǁSolutionǁisValidSudoku__mutmut_36': xǁSolutionǁisValidSudoku__mutmut_36, 
        'xǁSolutionǁisValidSudoku__mutmut_37': xǁSolutionǁisValidSudoku__mutmut_37, 
        'xǁSolutionǁisValidSudoku__mutmut_38': xǁSolutionǁisValidSudoku__mutmut_38, 
        'xǁSolutionǁisValidSudoku__mutmut_39': xǁSolutionǁisValidSudoku__mutmut_39, 
        'xǁSolutionǁisValidSudoku__mutmut_40': xǁSolutionǁisValidSudoku__mutmut_40, 
        'xǁSolutionǁisValidSudoku__mutmut_41': xǁSolutionǁisValidSudoku__mutmut_41, 
        'xǁSolutionǁisValidSudoku__mutmut_42': xǁSolutionǁisValidSudoku__mutmut_42, 
        'xǁSolutionǁisValidSudoku__mutmut_43': xǁSolutionǁisValidSudoku__mutmut_43, 
        'xǁSolutionǁisValidSudoku__mutmut_44': xǁSolutionǁisValidSudoku__mutmut_44, 
        'xǁSolutionǁisValidSudoku__mutmut_45': xǁSolutionǁisValidSudoku__mutmut_45, 
        'xǁSolutionǁisValidSudoku__mutmut_46': xǁSolutionǁisValidSudoku__mutmut_46, 
        'xǁSolutionǁisValidSudoku__mutmut_47': xǁSolutionǁisValidSudoku__mutmut_47, 
        'xǁSolutionǁisValidSudoku__mutmut_48': xǁSolutionǁisValidSudoku__mutmut_48, 
        'xǁSolutionǁisValidSudoku__mutmut_49': xǁSolutionǁisValidSudoku__mutmut_49, 
        'xǁSolutionǁisValidSudoku__mutmut_50': xǁSolutionǁisValidSudoku__mutmut_50, 
        'xǁSolutionǁisValidSudoku__mutmut_51': xǁSolutionǁisValidSudoku__mutmut_51, 
        'xǁSolutionǁisValidSudoku__mutmut_52': xǁSolutionǁisValidSudoku__mutmut_52, 
        'xǁSolutionǁisValidSudoku__mutmut_53': xǁSolutionǁisValidSudoku__mutmut_53, 
        'xǁSolutionǁisValidSudoku__mutmut_54': xǁSolutionǁisValidSudoku__mutmut_54, 
        'xǁSolutionǁisValidSudoku__mutmut_55': xǁSolutionǁisValidSudoku__mutmut_55, 
        'xǁSolutionǁisValidSudoku__mutmut_56': xǁSolutionǁisValidSudoku__mutmut_56, 
        'xǁSolutionǁisValidSudoku__mutmut_57': xǁSolutionǁisValidSudoku__mutmut_57, 
        'xǁSolutionǁisValidSudoku__mutmut_58': xǁSolutionǁisValidSudoku__mutmut_58, 
        'xǁSolutionǁisValidSudoku__mutmut_59': xǁSolutionǁisValidSudoku__mutmut_59, 
        'xǁSolutionǁisValidSudoku__mutmut_60': xǁSolutionǁisValidSudoku__mutmut_60, 
        'xǁSolutionǁisValidSudoku__mutmut_61': xǁSolutionǁisValidSudoku__mutmut_61, 
        'xǁSolutionǁisValidSudoku__mutmut_62': xǁSolutionǁisValidSudoku__mutmut_62, 
        'xǁSolutionǁisValidSudoku__mutmut_63': xǁSolutionǁisValidSudoku__mutmut_63, 
        'xǁSolutionǁisValidSudoku__mutmut_64': xǁSolutionǁisValidSudoku__mutmut_64, 
        'xǁSolutionǁisValidSudoku__mutmut_65': xǁSolutionǁisValidSudoku__mutmut_65, 
        'xǁSolutionǁisValidSudoku__mutmut_66': xǁSolutionǁisValidSudoku__mutmut_66, 
        'xǁSolutionǁisValidSudoku__mutmut_67': xǁSolutionǁisValidSudoku__mutmut_67, 
        'xǁSolutionǁisValidSudoku__mutmut_68': xǁSolutionǁisValidSudoku__mutmut_68, 
        'xǁSolutionǁisValidSudoku__mutmut_69': xǁSolutionǁisValidSudoku__mutmut_69
    }

    def isValidSudoku(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSolutionǁisValidSudoku__mutmut_orig"), object.__getattribute__(self, "xǁSolutionǁisValidSudoku__mutmut_mutants"), *args, **kwargs)
        return result 

    isValidSudoku.__signature__ = _mutmut_signature(xǁSolutionǁisValidSudoku__mutmut_orig)
    xǁSolutionǁisValidSudoku__mutmut_orig.__name__ = 'xǁSolutionǁisValidSudoku'


